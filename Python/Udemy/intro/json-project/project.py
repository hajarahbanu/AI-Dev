import json

with open("questions.json", "r") as file:
    content = file.read()

print(type(content))

data = json.loads(content)
# the above function converts the string into a list of dictionaries

print(type(data))
print(data)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_answer = int(input("enter your answer: "))
    question["user_answer"] = user_answer
    if question["user_answer"] == question["answer"]:
        score +=1


print("your score is", score, "out of", len(data))