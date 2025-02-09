size = input("Choose a coffee size (Small, Medium, Large): ").strip().lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").strip().lower()

if size in ["small", "medium", "large"]:
    order = f"{size.capitalize()} coffee"
    
    if extra_shot == "yes":
        order += " with an extra shot of espresso"

    print(f"Your order: {order}")
else:
    print("Invalid size. Please choose Small, Medium, or Large.")
