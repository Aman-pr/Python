class Car:
    def fuel_type(self):
        return "This car uses gasoline or diesel."

class ElectricCar(Car):
    def fuel_type(self):
        return "This car runs on electricity."

def show_fuel_type(vehicle):
    print(vehicle.fuel_type())

show_fuel_type(Car())  
show_fuel_type(ElectricCar())  
