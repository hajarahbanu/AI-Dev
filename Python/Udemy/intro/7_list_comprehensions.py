todos = []

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"
            file = open('file_handling/sample1.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)
            
            file = open('file_handling/sample1.txt', 'w')
            file.writelines(todos)
        
        case "show" :
            file = open("file_handling/sample1.txt", "r")
            todos = file.readlines()
            file.close()

            # new_todos = []

            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            new_todos = [item.strip('\n') for item in todos]
            
            for index, item in enumerate(new_todos):
                row = f"{index + 1} - {item}"
                print(row)
        
        case "edit" :
            ind = int(input("number of the todo to edit: "))
            ind = ind - 1
            new_todo = input("enter a new todo: ") + "\n"
            todos[ind] = new_todo
        
        case "complete":
            ind = int(input("number of the todo to complete: "))
            ind = ind - 1
            todos.pop(ind)
        
        case "exit":
            break
    
print("bye!")   