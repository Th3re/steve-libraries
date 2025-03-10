import copy
import datetime
from typing import Optional

from ..representation.pretty import PrettyPrint


class Event(PrettyPrint):
    def __init__(self,
                 identifier: str,
                 html_link: str,
                 summary: Optional[str],
                 location: Optional[str],
                 start_time: datetime,
                 end_time: datetime,
                 status: Optional[str]):
        self.status = status
        self.end_time = end_time
        self.start_time = start_time
        self.location = location
        self.summary = summary
        self.html_link = html_link
        self.identifier = identifier

    @staticmethod
    def __parse_time(time_string):
        # Example time_string 2020-04-23T16:30:00+02:00
        timestamp = time_string.get('dateTime')
        if not timestamp:
            return None
        return datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S%z')

    def to_json(self):
        body = copy.copy(vars(self))
        format = '%Y-%m-%dT%H:%M:%S%z'
        body['start_time'] = datetime.datetime.strftime(self.start_time, format)
        body['end_time'] = datetime.datetime.strftime(self.end_time, format)
        return body

    @staticmethod
    def from_json(dictionary):
        start_time = Event.__parse_time({'dateTime': dictionary['start_time']})
        end_time = Event.__parse_time({'dateTime': dictionary['end_time']})
        return Event(identifier=dictionary['identifier'],
                     html_link=dictionary['html_link'],
                     summary=dictionary.get('summary'),
                     location=dictionary.get('location'),
                     start_time=start_time,
                     end_time=end_time,
                     status=dictionary.get('status'))

    @staticmethod
    def from_dict(dictionary):
        start_time = Event.__parse_time(dictionary['start'])
        end_time = Event.__parse_time(dictionary['end'])
        return Event(identifier=dictionary['id'],
                     html_link=dictionary['htmlLink'],
                     summary=dictionary.get('summary'),
                     location=dictionary.get('location'),
                     start_time=start_time,
                     end_time=end_time,
                     status=dictionary.get('status'))
