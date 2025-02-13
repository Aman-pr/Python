class Car:
    def __init__(self, name, c_type):
        print("This is the init method")
        self.name = name
        self.c_type = c_type
        print(self.name)
        print(self.c_type)

    def type_car(self, brand, name):
        self.brand = brand 
        self.name = name    
        print(f"This is a {self.brand} {self.name}")
    
    def display_car(self):
        print(f"the name of brand is {self.brand}")

my_car = Car("Model S", "Electric")

my_car.type_car("Tesla", "Model S")
my_car.display_car()
