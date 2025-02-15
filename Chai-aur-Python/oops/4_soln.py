class Car:
    def __init__(self, name, c_type):
        print("This is the init method")
        self.name = name
        self.c_type = c_type
        self.__brand = None  
        print(self.name)
        print(self.c_type)

    def type_car(self, brand, name):
        self.__brand = brand  
        self.name = name    
        print(f"This is a {self.__brand} {self.name}")

    def get_brand(self):
        """Getter method for brand"""
        return self.__brand


my_car = Car("Model S", "Electric")


my_car.type_car("Tesla", "Model S")


print("Brand:", my_car.get_brand())
