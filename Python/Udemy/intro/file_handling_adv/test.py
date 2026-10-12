# todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"
            with open('sample.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)
            
            with open('sample.txt', 'w') as file:
                file.writelines(todos)
        
        case "show" :
            with open("sample.txt", "r") as file:
                todos = file.readlines()
            
            for index, item in enumerate(todos):
                row = f"{index + 1} - {item}"
                print(row)
        
        case "edit" :
            ind = int(input("number of the todo to edit: "))
            ind = ind - 1

            with open('sample.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("enter a new todo: ") + "\n"
            todos[ind] = new_todo

            with open('sample.txt', 'w') as file:
                file.writelines(todos)
        
        case "complete":
            ind = int(input("number of the todo to complete: "))
            ind = ind - 1

            with open('sample.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(ind)

            with open('sample.txt', 'w') as file:
                file.writelines(todos)
        
        case "exit":
            break
    
print("bye!")   