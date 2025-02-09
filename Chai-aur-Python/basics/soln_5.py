weather_activities = {
    "sunny": "Go for a walk",
    "rainy": "Read a book",
    "snowy": "Build a snowman",
    "cloudy": "Take photos",
    "windy": "Fly a kite",
    "stormy": "Stay indoors and watch a movie"
}

weather = input("Enter the current weather (sunny, rainy, snowy, cloudy, windy, stormy): ").strip().lower()

if weather in weather_activities:
    print(f"Suggested activity: {weather_activities[weather]}")
else:
    print("Sorry, I don't have an activity suggestion for that weather.")
