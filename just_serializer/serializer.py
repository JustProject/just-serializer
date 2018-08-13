from .field import Field


class Empty:
    pass


class Serializer(Field):
    model = None
    fields = tuple()

    def __init__(self, instance=None, data=Empty, **kwargs):
        self.instance = instance
        if data is not Empty:
            self.initial_data = data
        self.partial = kwargs.pop('partial', False)
        self.many = kwargs.pop('many', False)
        super(Serializer, self).__init__(**kwargs)

    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        pass
