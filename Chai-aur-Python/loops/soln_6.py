num = int(input("Enter a number: "))  
fact = 1  
i = num  

while i > 1:  
    fact *= i  
    i -= 1  

print(f"Factorial of {num} is {fact}")  
