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
        
    elif user_action.startswith("edit"):
        ind = int(user_action[5:])
        ind = ind - 1

        with open('sample.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("enter a new todo: ") + "\n"
        todos[ind] = new_todo

        with open('sample.txt', 'w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("complete"):
        ind = int(user_action[9:])
        ind = ind - 1

        with open('sample.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(ind)

        with open('sample.txt', 'w') as file:
            file.writelines(todos)
        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("command is not valid")
    
print("bye!")   