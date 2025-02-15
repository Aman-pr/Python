class Parent:
    def __init__(self):
        self.init = "this is init class"
        
    def class_Function(self):
        self.var = "this is class one function"


class Child(Parent):
    def __init__(self):
        super().__init__()  
        super().class_Function()  

    def child_function(self):
        print("This is child function class")
        print(self.init)  
        print(self.var)   


def main():
    print("This is main function")
    child_class = Child()
    child_class.child_function()


main()
