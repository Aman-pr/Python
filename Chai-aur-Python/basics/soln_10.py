pet_food_recommendations = {
    "dog": {
        "young": "Puppy food",
        "adult": "Adult dog food",
        "senior": "Senior dog food"
    },
    "cat": {
        "young": "Kitten food",
        "adult": "Adult cat food",
        "senior": "Senior cat food"
    }
}

pet = input("Enter the pet species (Dog/Cat): ").strip().lower()
age = int(input("Enter the pet's age in years: "))

if pet in pet_food_recommendations:
    if age < 2:
        food = pet_food_recommendations[pet]["young"]
    elif 2 <= age <= 5:
        food = pet_food_recommendations[pet]["adult"]
    else:
        food = pet_food_recommendations[pet]["senior"]
    
    print(f"Recommended food: {food}")
else:
    print("Sorry, I don't have recommendations for that pet.")

