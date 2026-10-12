# todos = []


while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    # if "add" in user_action this can't handle "edit add a new message" but if user_action.startswith("add") this can handle it
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        with open('sample.txt', 'r') as file:
            todos = file.readlines()

            todos.append(todo)
            
        with open('sample.txt', 'w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("show"):
        with open("sample.txt", "r") as file:
            todos = file.readlines()
            
        for index, item in enumerate(todos):
            row = f"{index + 1} - {item}"
            print(row)

    
    # below handled the error when user enters "edit" without a number or with a non-integer value and when user enters "complete" without a number or with a non-integer value or with a number that is out of range
    elif user_action.startswith("edit"):
        try:
            ind = int(user_action[5:])
            ind = ind - 1

            with open('sample.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("enter a new todo: ") + "\n"
            todos[ind] = new_todo

            with open('sample.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("your command is not valid")
            continue
    
    # if user enters "complete" without a number or with a non-integer value or with a number that is out of range, it will raise an IndexError which we can catch and handle it by printing a message to the user and continue the loop 
    elif user_action.startswith("complete"):
        try:
            ind = int(user_action[9:])
            ind = ind - 1

            with open('sample.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(ind)

            with open('sample.txt', 'w') as file:
                file.writelines(todos)
        except IndexError:
            print("there is no item with that number")
            continue
        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("command is not valid")
    
print("bye!")   