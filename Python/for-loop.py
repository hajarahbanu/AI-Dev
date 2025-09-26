
# for loop usage
expense = [2345,2145,1254,2390,5678]
month = ['jan','feb','mar','apr','may']
total = 0
for i in range(len(month)):
    print(month[i],":", expense[i])
    total += expense[i]

print("total expense: ", total)

# break usage
key_location = "tv stand"
locations = ["garage","scooter","pocket","tv stand","kitchen","sofa"]

for i in locations:
    if i == key_location:
        print("key is found")
        break
    else:
        print("key is not found")

# continue usage
for i in range(1,21):
    if i%2 == 0 :
        continue
    print(i*i)
