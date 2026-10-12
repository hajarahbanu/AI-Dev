todos = []

while True:
    user_input = input("type show, add or exit")

    match user_input:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        
        case 'show':
            for item in todos:
                print(item)
        
        case 'exit':
            break
    
print('bye')
