#This is solution 1 of question
List = {
    "Child": {},
    "Teenager": {},
    "Adult": {},
    "Senior": {}
}
choice = "y"
while choice.lower() == "y": 
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 13:
        List["Child"][name] = age
    elif 13 <= age <= 19:  
        List["Teenager"][name] = age
    elif 20 <= age <= 59:  
        List["Adult"][name] = age  
    elif age >= 60:  
        List["Senior"][name] = age   
    else:
        print("Error: Wrong input type")
    choice = input("Do you want to continue? (y/n): ")
print("\nFinal List:", List)

