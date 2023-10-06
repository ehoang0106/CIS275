class Item:

    def __init__(self, description, price):
        self._description = description
        self._price = price

    def __str__(self):
        
        return_string = f"{self._description} - price: ${self._price:.2f}"
    
        return return_string
