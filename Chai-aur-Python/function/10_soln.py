def rec_fun(n):
    if n % 2 == 0:  
        return True
    else:
        return False

def main():
    print("This is a recursion program")
    choice = True 

    while choice:
        n = int(input("Enter a number: "))  
        result = rec_fun(n)  
        print("True") if result else print("False")
        choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if choice != "yes": 
            choice = False

main()
