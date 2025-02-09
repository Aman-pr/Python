distance = float(input("Enter the distance in km: "))

if distance < 3:
    transport = "Walk"
elif 3 <= distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print(f"Suggested mode of transportation: {transport}")
