class Car:
    def fuel_type(self):
        return "This car uses gasoline or diesel."

class ElectricCar(Car):
    def fuel_type(self):
        return "This car runs on electricity."

my_tesla = ElectricCar()

print(isinstance(my_tesla, ElectricCar))  
print(isinstance(my_tesla, Car))         
print(isinstance(my_tesla, object))     
