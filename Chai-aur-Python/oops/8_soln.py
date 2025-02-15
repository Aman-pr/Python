class Car:
    car_count = 0  

    def __init__(self, model):
        self._model = model  
        Car.car_count += 1  

    @property
    def model(self):
        return self._model  

    def fuel_type(self):
        return "This car uses gasoline or diesel."

    @staticmethod
    def general_description():
        return "A car is a wheeled motor vehicle used for transportation."

class ElectricCar(Car):
    def fuel_type(self):
        return "This car runs on electricity."

def show_fuel_type(vehicle):
    print(vehicle.fuel_type())

car1 = Car("Toyota Corolla")
car2 = Car("Honda Civic")
electric_car1 = ElectricCar("Tesla Model S")

show_fuel_type(car1)  
show_fuel_type(electric_car1)

print("Total cars created:", Car.car_count)
print(Car.general_description())

print("Car 1 model:", car1.model)

# Attempting to modify the model (should raise an error)
# car1.model = "Ford Mustang"  # This will cause an AttributeError
