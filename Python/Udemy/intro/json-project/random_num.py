import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))
random_number = random.randrange(lower_bound, upper_bound+1)

print("The random number between", lower_bound, "and", upper_bound, "is:", random_number)