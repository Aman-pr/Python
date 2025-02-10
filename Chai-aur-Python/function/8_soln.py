def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    print("Enter details (type 'stop' to finish):")
    data = {}
    while True:
        key = input("Enter key: ")
        if key.lower() == "stop":
            break
        value = input("Enter value: ")
        data[key] = value  

    print("\nEntered Data:")
    print_kwargs(**data)  

main()
