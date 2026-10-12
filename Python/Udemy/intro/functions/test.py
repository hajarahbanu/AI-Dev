#  --- getting average from a file containing numbers ---

# def get_average():
#     with open('sample.txt', 'r') as file:
#         values = file.readlines()
    
#     data = values[1:]

#     data_float = [float(d) for d in data]

#     avg = sum(data_float) / len(data_float)
    
#     return avg

# average = get_average()
# print(average)

#  --- converting feet inches to meters ---
# feet_inches = input('Enter feet and inches: ')

# def convert_to_meters(feet_inches):
#     parts = feet_inches.split(" ")
#     feet = float(parts[0])
#     inches = float(parts[1])
#     meters = (feet * 0.3048) + (inches * 0.0254)
#     return f"{feet} feet and {inches} inches is equal to {meters} meters."


# print(convert_to_meters(feet_inches))

def prepare(text):
    text = text.title()
    text = text.strip()
    return text
    
print(prepare("hello    "))