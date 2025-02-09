fruit_ripeness = {
    "banana": {
        "green": "Unripe",
        "yellow": "Ripe",
        "brown": "Overripe"
    },
    "apple": {
        "green": "Unripe",
        "red": "Ripe",
        "dark brown": "Overripe"
    },
    "mango": {
        "green": "Unripe",
        "yellow": "Ripe",
        "black": "Overripe"
    }
}

fruit = input("Enter the fruit name (banana, apple, mango): ").strip().lower()
color = input("Enter the fruit color: ").strip().lower()

if fruit in fruit_ripeness:
    if color in fruit_ripeness[fruit]:
        ripeness = fruit_ripeness[fruit][color]
        print(f"The {fruit} is {ripeness}.")
    else:
        print("Sorry, I don't have ripeness information for that color.")
else:
    print("Sorry, I don't have ripeness information for that fruit.")
