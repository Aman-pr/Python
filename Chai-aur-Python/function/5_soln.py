def greet(name="Guest"):
    print(f"Hello, {name}!")

def main():
    user_name = input("Enter your name (or press Enter to skip): ").strip()
    if user_name == "":
        greet()  # Uses default "Guest"
    else:
        greet(user_name)

main()
