def calculate_area(b,h):
    print("__name__: ", __name__)
    return 1/2 * (b * h)


if __name__ == "__main__":
    print("I am in area.py")
    a = calculate_area(10,20)
    print("area : " , a)