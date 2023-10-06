class Fraction:

    def __init__(self, numerator, denominator):

        if denominator == 0:
            raise ValueError("Demoninator cannot be 0!")
        
        self._numerator = numerator
        self._denominator = denominator

    
    def __eq__(self, other):
        return self._numerator * other._denominator == other._numerator * self._denominator

    def __gt__(self, other):
        return self._numerator * other._denominator > other._numerator * self._denominator

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"
    
