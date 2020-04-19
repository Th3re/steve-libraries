import typing


ChannelEnvironment = typing.NamedTuple('ChannelEnvironment', [('exchange', str),
                                                              ('topic', str)])


RabbitEnvironment = typing.NamedTuple('RabbitEnvironment', [('host', str),
                                                            ('port', int),
                                                            ('connection_attempts', int),
                                                            ('retry_delay', int)])
