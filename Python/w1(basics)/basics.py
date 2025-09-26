
# 1. swap two numbers
# Using a temporary variable
a = 2
b = 5
temp = a
a = b
b = temp
print(a, b)

# OR Pythonic way
a, b = b, a
print(a, b)

# or 
c = a + b
a = c - a
b = c - b
print(a, b)

# 2. to get user input and print
name = input("enter your name:")
print("hello" , name)


# 3. check even or odd
num = int(input("enter a number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
# or
print("even" if num % 2 == 0 else "odd")

# 4. print multiplication table
for i in range(1,11):
    print(num , "x" , i , "=", num*i)

# 5. find largest of three numbers
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))   
num3 = int(input("enter third number:"))
if num1 >= num2 and num1 >= num3:
    print(num1 , "is the largest")
elif num2 >= num1 and num2 >= num3:
    print(num2 , "is the largest")
else:
    print(num3 , "is the largest")

# or    
print(max(num1, num2, num3), "is the largest")


# temp conversion to celsius to fahrenheit
temp_c = float(input("enter temperature in celsius:"))
temp_f = (temp_c * 9/5) + 32
print(temp_c , "celsius is" , temp_f , "fahrenheit")

# factorial of a number
base = 1 
for i in range(1,num+1):
    base = base * i
print("factorial of" , num , "is" , base)

# count vowels in a string and reverse the string
vowels = ['a', 'e', 'i', 'o', 'u']
string = input("enter a string:")
count = 0
for char in string:
    if char.lower() in vowels:
        count += 1
print("number of vowels in the string is:" , count) 

vowels = "aeiou"
string = input("enter a string:")
count = 0
for char in string.lower():
    if char in vowel:
        count += 1
print("number of vowels in the string is:", count)


# reverse the string
rev_string = string[::-1]
print("reversed string is:" , rev_string)

# check palindrome
print("palindrom " if string == rev_string else "not a palindrome")




