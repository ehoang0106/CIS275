class Array:

    def __init__(self, capacity):
        """ Capacity is the static size of the array. Each index is initialized to None """
        self._items =[]
        for i in range(capacity):
            self._items.append(None)

        self._logical_size = 0
    
    def get_logical_size(self):
        return self._logical_size

    def __len__(self):
        return len(self._items)
    
    def __str__(self):
        return str(self._items)
    
    def __iter__(self):
        """Return an iterator over the Array"""
        return iter(self._items)
    
    def __getitem__(self, index):
        """Return the item at the given index"""
        return self._items[index]
    
    def __setitem__(self, index, new_item):
        
        #If the client tries to update an index further than the first logically empty index of the array, raise an error.
        if index > self._logical_size or index < 0:
            raise IndexError(f"Index {index} is beyond logical size")
        #If the client tries to set an index to None, make sure it is the last logically filled index of the array.
        elif new_item is None and index != self._logical_size - 1:
            raise IndexError(f"Can't set value at index {index} to None")
        elif self._items[index] is None and new_item is not None:
            self._logical_size += 1
        elif self._items[index] is not None and new_item is None:
            self._logical_size -= 1
        
        self._items[index] = new_item

    def __eq__(self, other):
        if not isinstance(other, Array):
            return False
        if self._logical_size != other.get_logical_size():
            return False
        for i in range (self._logical_size):
            if self._items[i] != other[i]:
                return False
        return True
