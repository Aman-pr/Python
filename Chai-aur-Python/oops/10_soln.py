class Car:
    def __init__(self, brand):
        self.brand = brand

    def fuel_type(self):
        return "This car uses gasoline or diesel."

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity  

    def battery_info(self):
        return f"Battery capacity: {self.capacity} kWh"

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower  

    def engine_info(self):
        return f"Engine horsepower: {self.horsepower} HP"

class ElectricCar(Car, Battery, Engine):  
    def __init__(self, brand, capacity, horsepower):
        Car.__init__(self, brand)  
        Battery.__init__(self, capacity)  
        Engine.__init__(self, horsepower)  

    def fuel_type(self):
        return "This car runs on electricity."

my_tesla = ElectricCar("Tesla", 100, 450)

print(my_tesla.fuel_type())        
print(my_tesla.battery_info())     
print(my_tesla.engine_info())      
print("Brand:", my_tesla.brand)     
