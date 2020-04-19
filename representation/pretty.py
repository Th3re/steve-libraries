

class PrettyPrint:
    def __repr__(self):
        values = ', '.join([f'{key}: \"{value}\"' for key, value in self.__dict__.items()])
        return f'<{self.__class__.__name__}>[{values}]'
