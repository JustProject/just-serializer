class Field(object):
    default_validators = []

    def __init__(self, validators=None):
        self.parent = None
        self.field_name = None

        if validators is not None:
            self.validators = validators[:]

    def bind(self, field_name, parent):
        self.field_name = field_name
        self.parent = parent

    @property
    def validators(self):
        if not hasattr(self, '_validators'):
            self._validators = self.get_validators()
        return self._validators

    @validators.setter
    def validators(self, validators):
        self._validators = validators

    def get_validators(self):
        return self.default_validators[:]

    def to_internal_value(self, data):
        """
        Transform the *incoming* primitive data into a native value.
        """
        raise NotImplementedError(
            '{cls}.to_internal_value() must be implemented.'.format(
                cls=self.__class__.__name__
            )
        )

    def to_representation(self, value):
        """
        Transform the *outgoing* native value into primitive data.
        """
        raise NotImplementedError(
            '{cls}.to_representation() must be implemented for field '
            '{field_name}.'.format(
                cls=self.__class__.__name__,
                field_name=self.field_name,
            )
        )
