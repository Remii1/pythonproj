class Calculation1:
    def add(self, a, b):
        return a+b

class Calculation2:
    def subtract(self, a, b):
        return a-b

class Calculation3:
    def multiply(self, a, b):
        return a*b

class Calculation(Calculation3,Calculation2,Calculation1):
    def divide(self, a, b):
        return a/b

c = Calculation()
print(c.subtract(56,8))
print(c.divide(65,5))