class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    def age(self):
        current_year = 2023

        return current_year - self._year


    def __str__(self):
        
        return_string = "--Car specs--\n"
        return_string += f"Make: {self._make}\n"
        return_string += f"Model: {self._model}\n"
        return_string += f"Year: {self._year}\n"
        return_string += f"Age: {self.age()} years old\n"
        
        return return_string

