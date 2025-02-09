def multiply(a, b):
    if a.isdigit():
        a = int(a)
    if b.isdigit():
        b = int(b)
    
    if isinstance(a, int) and isinstance(b, int):
        return a * b
    if isinstance(a, str) and isinstance(b, int):
        return a * b
    if isinstance(b, str) and isinstance(a, int):
        return b * a
    
    return "Invalid input"

def main():
    num1 = input("Enter first input: ")
    num2 = input("Enter second input: ")

    result = multiply(num1, num2)
    print("Result:", result)

main()
