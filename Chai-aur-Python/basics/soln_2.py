#This is solution 2 of question
import datetime
day=datetime.date.today().strftime("%A")
choice = "y"
sum=0
while choice.lower() == "y": 
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    if age < 18:
       print("Cost for child is $8")
       if day=="Wednesday":
           print("For wednesday you got offer of ticket price 6")
           sum=sum+6
       else:   
           sum=sum+8
       
    elif 18 <= age:  
        print("Cost for Adult is $12")
        if day=="Wednesday":
           sum=sum+10
           print("For wednesday you got offer of ticket price 10")
        else:   
           sum=sum+12
    else:
        print("Error: Wrong input type")
    choice = input("Do you want to continue? (y/n): ")
print("the total amountto be payed : ",sum)
