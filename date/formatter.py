import abc
import datetime

DATE_FORMAT = '%Y-%m-%d'
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S%z'


class Formatter(abc.ABC):
    @abc.abstractmethod
    def format_date(self, date: datetime.datetime) -> str:
        pass

    @abc.abstractmethod
    def parse_date(self, date: str) -> datetime.datetime:
        pass


class DatetimeFormatter(Formatter):
    def format_date(self, date: datetime.datetime) -> str:
        return date.strftime(DATETIME_FORMAT)

    def parse_date(self, date: str) -> datetime.datetime:
        return datetime.datetime.strptime(date, DATETIME_FORMAT)


class DateFormatter(Formatter):
    def format_date(self, date: datetime.datetime) -> str:
        return date.strftime(DATE_FORMAT)

    def parse_date(self, date: str) -> datetime.datetime:
        return datetime.datetime.strptime(date, DATE_FORMAT)