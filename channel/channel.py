import abc
import enum


class Message(abc.ABC):
    @abc.abstractmethod
    def serialize(self):
        pass

    @classmethod
    @abc.abstractmethod
    def deserialize(cls, raw):
        pass


class ChannelResponse:
    class Status(enum.Enum):
        OK = "OK"
        ERROR = "ERROR"

    def __init__(self, message: str, status: Status):
        self.message = message
        self.status = status


class Channel(abc.ABC):
    @abc.abstractmethod
    def send(self, topic, data) -> ChannelResponse:
        pass
