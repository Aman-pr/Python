def first_unique_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None  


input_str = input("Enter a string: ")
result = first_unique_char(input_str)

print("First non-repeated character:", result if result else "None")
