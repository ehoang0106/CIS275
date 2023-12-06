from AbstractCollection import AbstractCollection
from Array import Array


class MaxHeap(AbstractCollection):


    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._heap = Array(MaxHeap.DEFAULT_CAPACITY)
        AbstractCollection.__init__(self)
        self._numitems = 0
    
    def __len__(self):
        return self._numitems

    def peek(self):

        if self.is_empty():
            raise IndexError("Heap is empty!")
        return self._heap[0]
    
    

    
    def resize(self):
        new_size = len(self._heap) * 2
        new_array = Array(new_size)
        for i in range(len(self._heap)):
            new_array[i] = self._heap[i]
        self._heap = new_array
    
    def add(self, item):
        if len(self) == len(self._heap):
            self.resize()
        self._heap[len(self)] = item
        cur_index = len(self)

        while cur_index > 0:
            parent_index = (cur_index - 1) // 2
            parent_item = self._heap[parent_index]
            if parent_item <= item:
                break
            self._heap[cur_index] = parent_item
            self._heap[parent_index] = item
            cur_index = parent_index

        self._numitems += 1


    def pop(self):
        if self.is_empty():
            raise IndexError("Heap is empty!")
        
        top_item = self._heap[0]
        bottom_item = self._heap[self._numitems - 1]

        self._heap[0] = bottom_item

        last_valid_index = self._numitems - 2

        cur_index = 0


        while True:
            left_child_index = 2 * cur_index + 1
            right_child_index = 2 * cur_index + 2
            if left_child_index > last_valid_index:
                break


            if right_child_index > last_valid_index:
                min_child_index = left_child_index
            else:
                left_child = self._heap[left_child_index]
                right_child = self._heap[right_child_index]

            if left_child < right_child:
                min_child_index = left_child_index
            else:
                min_child_index = right_child_index

            min_child = self._heap[min_child_index]

            if bottom_item <= min_child:
                break

            self._heap[cur_index] = min_child
            self._heap[min_child_index] = bottom_item
            cur_index = min_child_index

        self._numitems -= 1
        return top_item