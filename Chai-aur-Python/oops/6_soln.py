class Car:
    car_count = 0  

    def __init__(self):
        Car.car_count += 1  

    def fuel_type(self):
        return "This car uses gasoline or diesel."

class ElectricCar(Car):
    def fuel_type(self):
        return "This car runs on electricity."  

def show_fuel_type(vehicle):
    print(vehicle.fuel_type())

car1 = Car()
car2 = Car()
electric_car1 = ElectricCar()
electric_car2 = ElectricCar()

show_fuel_type(car1)  
show_fuel_type(electric_car1)

print("Total cars created:", Car.car_count)
