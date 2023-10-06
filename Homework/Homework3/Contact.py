class Contact:
    def __init__(self, name, phone_number):

        self._name = name
        self._phone_number = phone_number


    def __str__(self):
        return f"{self._name}: {self._phone_number}"
    
    