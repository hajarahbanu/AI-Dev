Adam = [2341,234,675,3432]
Bob = [8474,764,342,452]

def calculate_total(expense):
    total = 0 
    for i in expense:
        total += i 
    return total

print("Adam's total expense : " , calculate_total(Adam) )
print("Bob's total expense : " , calculate_total(Bob) )

