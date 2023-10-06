class Counter:
    instances = 0


    def __init__(self):

        Counter.instances += 1
        self._value = 0


    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, val):
        self._value = val