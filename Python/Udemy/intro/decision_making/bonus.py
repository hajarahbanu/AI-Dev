# password authentication

password = input("enter your password: ")
result = {}

# condition 1 = password should be at least 8 characters

if len(password) >= 8 :
    result["length"] = True
else:
    result["length"] = False

# condition 2 = password should contain at least one number

digit = False

for char in password:
    if char.isdigit():
        digit = True

result["digit"] = digit

# condition 3 = at least one uppercase letter

upppercase = False

for char in password:
    if char.isupper():
        upppercase = True

result["uppercase"] = upppercase

print(result)
print(result.values())

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password.")