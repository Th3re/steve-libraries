import logging

import pika.exceptions

from .environment import ChannelEnvironment, RabbitEnvironment
from ...channel.channel import Channel, ChannelResponse

LOG = logging.getLogger(__name__)


class RabbitChannel(Channel):
    __exchange_type = 'topic'

    def __init__(self, channel_env: ChannelEnvironment, rabbit_env: RabbitEnvironment):
        self.channel = None
        self.connection = None
        self.exchange = channel_env.exchange
        self.topic = channel_env.topic
        self.rabbit = rabbit_env

    def _create_connection(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=self.rabbit.host,
            port=self.rabbit.port,
            connection_attempts=self.rabbit.connection_attempts,
            retry_delay=self.rabbit.retry_delay
        ))
        channel = self.connection.channel()
        return channel

    def _send_attempt(self, topic, data) -> ChannelResponse:
        self.channel.exchange_declare(exchange=self.exchange, exchange_type=self.__exchange_type)
        routing_key = topic if self.topic == '' else f'{self.topic}.{topic}'
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=routing_key,
            body=data,
        )
        LOG.info(f'Sent {data} to {routing_key}')
        return ChannelResponse(
            message=f"Message uploaded to exchange: \"{self.exchange}\", topic \"{routing_key}\"",
            status=ChannelResponse.Status.OK,
        )

    def send(self, topic, data) -> ChannelResponse:
        try:
            return self._send_attempt(topic, data)
        except Exception as amqp_error:
            LOG.error(f'Send attempt error: {amqp_error}')
            try:
                self.channel = self._create_connection()
                return self._send_attempt(topic, data)
            except Exception as general_exception:
                LOG.error(f'Unexpected exception after reconnecting to rabbit: {general_exception}')
                return ChannelResponse(
                    message=f"Cannot publish message to {self.topic}",
                    status=ChannelResponse.Status.ERROR,
                )

    @staticmethod
    def create(channel_env: ChannelEnvironment, rabbit_env: RabbitEnvironment):
        return RabbitChannel(channel_env, rabbit_env)
