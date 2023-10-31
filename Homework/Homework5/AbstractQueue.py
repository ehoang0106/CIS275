from Array import Array
from AbstractCollection import AbstractCollection



class ArrayQueue(AbstractCollection):
    #initial capity = 10
    CAPACITY = 10


    def __init__(self):
        AbstractCollection.__init__(self)
        
        self._items = Array(ArrayQueue.CAPACITY)
        self._front = 0
        self._back = 0




    def ensure_capacity(self):
        if self._size == len(self._items):
            temp_arr = Array(len(self._items)*10) #increase temporay array size x10 original array
            f = self._front

            for i in range(self._size):
                temp_arr[i] = self._items[f]

                f =(f+1) % len(self._items) #f+1 is increment the index "front" then % len(self._items) to make sure if we reached the last element which is index 9 (size array is 10), the next logical positen after 9 would be index 0 instead of 10.

            self._front = 0
            self._back = self._size
            self._items = temp_arr


    
    def add(self, item):
        self.ensure_capacity()
        self._items[self._back] = item
        self._back = (self._back + 1) % len(self._items)
        self._size += 1



    def pop(self):
        if self.is_empty():
            raise "Queue is empty"
    
        temp = self._items[self._front]
        self._front = (self._front + 1) % len(self._items)
        self._size -= 1

        return temp
    
    def peak(self):
        if self.is_empty():
            raise "Queue is empty"
        
        return self._items[self._front]
    

    def clear(self):

        self._size = 0
        self._items = Array(ArrayQueue.CAPACITY)
        self._front = 0
        self._back = 0

    def print_queue(self):
        f = self._front
        if self.is_empty():
            print("Queue is empty!")
        else:

            for i in range(self._size):
                print(self._items[f])
                f = (f+1) % len(self._items)

