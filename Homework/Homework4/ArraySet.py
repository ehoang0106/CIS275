from Array import Array

from AbstractSet import AbstractSet


class ArraySet(AbstractSet):
    def __init__(self):
        self._data = Array(0)


    def add(self, item):
        if item not in self:
            self._data._items.append(item)

    def remove(self, item):
        if item in self:
            self._data._items.remove(item)

    def is_empty(self):
        return len(self._data) == 0


    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        #return str(self._data)
        return "[" + ", ".join(str(item) for item in sorted(self)) + "]"
    
    def __contains__(self, item):
        return item in self._data
    
    
    def __len__(self):
        return len(self._data) 