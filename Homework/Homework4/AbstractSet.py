

class AbstractSet:
    # def add(self, item):
    #     raise "Not Implemented"
    
    # def remove(self, item):
    #     raise "Not Implemented"

    # def __iter__(self):
    #     raise "Not Implemented"
        
    # def __contains__(self, item):
    #     raise "Not Implemented"
    
    # def __str__(self):
    #     raise "Not Implemented"
    

    # def is_empty(self):
    #     raise "Not Implemented"


    def intersection(self, other):
        new_set = self.__class__()

        for item in self:
            if item in other:
                new_set.add(item)
        

        return new_set
    

    def union(self, other):
        new_set = self.__class__()
        for item in self:
            new_set.add(item)

        for item in other:
            new_set.add(item)

        return new_set
    

    