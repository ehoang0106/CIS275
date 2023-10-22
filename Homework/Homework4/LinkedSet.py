from AbstractSet import AbstractSet
from Node import Node


class LinkedSet(AbstractSet):
    def __init__(self):
        self._head = None
        self._size = 0



    def add(self, item):
        if item not in self:
            new_node = Node(item, self._head)
            self._head = new_node
            self._size +=1 
    

    def remove(self, item):
        previous = None
        current = self._head


        while current and current._data != item:
            previous = current
            current = current._next

            if current:
                if previous:
                    previous._next = current._next
                else:
                    self._head = current._next

                self._size -= 1

    def is_empty(self):
        return self._size == 0
    
    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current:
            yield current._data
            current = current._next


    def __contains__(self, item):
        for i in self:
            if i == item:
                return True
        return False
    
    def __str__(self):
        #return "[" + ", ".join(str(item) for item in self) + "]"
        return "[" + ", ".join(str(item) for item in sorted(self)) + "]"

