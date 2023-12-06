from AbstractCollection import AbstractCollection
from MinHeap import MinHeap


class PriorityQueue(AbstractCollection):
    def __init__(self):
        super().__init__()
        self._min_heap = MinHeap()


    def add(self, item):
        self._min_heap.add(item)
        self._size = self._min_heap._numitems


    def pop(self):

        item = self._min_heap.pop()
        self._size = self._min_heap._numitems

        return item
    

    def peek(self):

        return self._min_heap.peek()