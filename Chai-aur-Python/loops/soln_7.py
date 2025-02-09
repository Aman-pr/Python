while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("Valid input:", num)
        break
    print("Invalid input! Please try again.")
