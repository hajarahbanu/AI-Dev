import Udemy.basics.functions as functions
import FreeSimpleGUI as gui

label = gui.Text("Type a task and press Enter to add it to the list.")
input_box = gui.InputText(tooltip="Enter your task here", key="todo")
add_button = gui.Button("Add Task", bind_return_key=True)

#add edit function
# 1. display the existing list of todos
todos_list = gui.Listbox(values=functions.get_todos(), key="todos",
                         enable_events=True, size=[45,10])

# 2. create an edit button
edit_button = gui.Button("Edit Task")

window = gui.Window("To-do List",
                     layout=[[label], [input_box, add_button],
                             [todos_list, edit_button]],
                     font=('Helvetica',20))
while True:
    event, value = window.read()
    print(1, event)
    print(2, value)
    print(3, value['todos'])
    match event:
        case "Add Task":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todo"].update(value="")
        case "Edit Task":
            todo_to_edit = value['todos'][0]
            new_todo = value['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            # here the window['todos'] refers to the listbox todos_list
            window['todos'].update(values=todos)

        case 'todos':
            # here the window['todo'] referes to the inputbox
            window['todo'].update(value=value['todos'][0])

        case gui.WIN_CLOSED:
            break
    

window.close()
