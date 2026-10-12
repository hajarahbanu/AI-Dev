# bear.txt | members.txt | multiple.txt | read_m_files | bug_testing1

# -- bear.txt --
# with open('bear.txt', 'r') as f:
#     content = f.readlines()
#     print(content)


# -- members.txt --
# member = input("add a new member: ")

# with open('members.txt', 'r') as f:
#     content = f.readlines()

# content.append(member)

# with open('members.txt', 'w') as f:
#     f.writelines(content)

# -- multiple.txt --
# filenames = ['doc.txt', 'report.txt', 'presentation.txt']

# for filename in filenames:
#     with open(filename , 'w') as f:
#         f.write("hello")

# -- read_m_files --
# list_of_files = ['a', 'b', 'c']

# for file in list_of_files:
#     with open(f"read_m_files/{file}.txt", 'r') as f:
#         content = f.read()
#         print(content)

# -- bug_testing1 --
# file = open("data.txt", 'w')
 
# file.write("100.12" + "\n")
# file.write("111.23" + "\n")
 
# file.close()
