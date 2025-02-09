def area_circum(rad):
    area = 3.14 * (rad ** 2)
    circum = 2 * 3.14 * rad
    return area, circum
    
def main():
    rad = float(input("Enter your radius: "))
    area, circum = area_circum(rad)  # Unpack the returned values
    print(f"The area of the circle is {area} and the circumference is {circum}")

main()
