from Item import Item
class Customer:
    def __init__(self, name, preferred_status):

        self._name = name
        self._preferred_status = preferred_status

        self._purchases = []
        #self._purchases = [None] * 5


    def make_purchase(self, description, price):
        if self._preferred_status == True:
            price = price * 0.9

        new_item = Item(description, price)

        self._purchases.append(new_item)
        
        # for i in range(len(self._purchases)):
        #     if self._purchases[i] is None:
        #         self._purchases[i] = new_item
        #         break


    def __str__(self):
        return_string = f"Customer name: {self._name}\nItems purchased:"

        for item in self._purchases:
            return_string += "\n" + str(item)

        return_string += "\n"
        return return_string