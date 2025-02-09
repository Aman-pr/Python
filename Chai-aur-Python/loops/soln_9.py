items = ["apple", "banana", "orange", "apple", "mango"]
seen = []

for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break
    seen.append(item)
else:
    print("All elements are unique")
