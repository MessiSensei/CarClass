
class Car:
    def __init__(self, b,c,p,m):
        self.brand = b
        self.color =  c
        self.price =  p
        self.model =  m
        print("Class has been constructed !!!")
    def drive(self):
        return f"The {self.color} {self.brand} is driving."

car1 =Car("Mercedes E-class ","Red",50000,2022)
car2 = Car("Porsche Macan","Blue",80000,2024)
car3 =Car("Toyota Pirius","Black", 30000,2023)

print(car1.drive())
print(car2.drive())
print(car3.drive())
