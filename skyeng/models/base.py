from types import SimpleNamespace


class Base:
    def __init__(self, session, info):
        self.session = session
        self.info = SimpleNamespace(**info)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, str(self))
