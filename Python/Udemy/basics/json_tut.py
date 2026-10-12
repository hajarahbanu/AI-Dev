import json

concerts = {}

concerts["Seventeen"] = {
   "group" : "seventeen",
   "venue" : "tokyo stadium",
   "time" : "6:30 pm"
}

concerts["Treasure"] = {
   "group" : "Treasure",
   "venue" : "Fukoka stadium",
   "time" : "7:30 pm"
}

concerts["BoyNextDoor"] = {
   "group" : "BoyNextDoor",
   "venue" : "Olympic stadium",
   "time" : "9:30 pm"
}

c = json.dumps(concerts)

print(c)
concert = json.loads(c)
print(concert)
# with open("C:\\AI-Development\\Python\\json_doc.txt", "w") as f:
#     f.write(c)


