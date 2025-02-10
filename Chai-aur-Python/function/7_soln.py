def sumtype(*args):
    return sum(args)

def main():
    print("This is function for the *args ")
    numbers = map(int, input("Enter numbers separated by space: ").split())
    print(f"tinhe sum of given number is {sumtype(*numbers)}")
main()