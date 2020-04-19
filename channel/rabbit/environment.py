from ...environment.environmentreader import EnvironmentReader


class ChannelEnvironment(EnvironmentReader):
    def __init__(self):
        super()
        self.exchange = self.get('exchange')
        self.topic = self.get('topic')


class RabbitEnvironment(EnvironmentReader):
    def __init__(self):
        super()
        self.host = self.get('host')
        self.port = self.get('port')
        self.connection_attempts = int(self.get('connection_attempts'))
        self.retry_delay = int(self.get('retry_delay'))