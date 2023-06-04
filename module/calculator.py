class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_numbers(self):
        total = self.num1 + self.num2
        return total
    
    def substract_numbers(self):
        total = self.num1 - self.num2
        return total
    
    def multiply_numbers(self):
        total = self.num1 * self.num2
        return total
    
    def division_numbers(self):
        total = self.num1 / self.num2
        return total
