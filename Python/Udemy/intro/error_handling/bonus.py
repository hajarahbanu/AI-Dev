try:
    width = float(input("Width: "))
    length = float(input("Length: "))

    if width == length:
        exit("That looks like a square...!")

    area_of_rectangle = width * length

    print(f"The area of the rectangle is {area_of_rectangle}")

except ValueError:
    print("enter a number next time")