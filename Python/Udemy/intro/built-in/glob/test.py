import glob

files = glob.glob("*.txt")
print(files) # here prints all the txt files in the current directory 

# ['glob_test.txt', 'ideas.txt', 'projects.txt']

for filepath in files:
    with open(filepath, "r") as file:
        print(file.read())