# todos = []
# docstrings are used to describe the purpose of a function and how to use it, they are written in triple quotes and they are placed at the beginning of the function body

# def get_todos(filepath):
#     """Reads the list of todos from a file and returns it."""
#     with open(filepath, 'r') as file_local:
#         todos_local = file_local.readlines()
#     return todos_local

# def write_todos(filepath, todos_arg):
#     """Writes the list of todos to a file."""
#     with open(filepath, 'w') as file_local:
#         file_local.writelines(todos_arg)

# -- i will be putting the functions in a separate file called functions.py and then i will import them in this file and use them here to keep the code organized and to avoid repetition of code when i want to use the same functions in different files --

from Udemy.basics.functions import get_todos, write_todos

#  here the functions file is a module

import time

now = time.strftime("%Y-%m-%d %H:%M:%S")

print("it is ", now)

print(help(get_todos))
print(help(write_todos))

while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()

    # if "add" in user_action this can't handle "edit add a new message" but if user_action.startswith("add") this can handle it
    
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos('tasks.txt')
        todos.append(todo + '\n')
        write_todos('tasks.txt', todos)

    elif user_action.startswith("show"):
        todos = get_todos('tasks.txt')
        for index, item in enumerate(todos):
            row = f"{index + 1} - {item}"
            print(row)

    
    # below handled the error when user enters "edit" without a number or with a non-integer value and when user enters "complete" without a number or with a non-integer value or with a number that is out of range
    elif user_action.startswith("edit"):
        try:
            ind = int(user_action[5:])
            ind = ind - 1

            todos = get_todos('tasks.txt')

            new_todo = input("enter a new todo: ") + "\n"
            todos[ind] = new_todo

            write_todos('tasks.txt', todos)

        except ValueError:
            print("your command is not valid")
            continue
    
    # if user enters "complete" without a number or with a non-integer value or with a number that is out of range, it will raise an IndexError which we can catch and handle it by printing a message to the user and continue the loop 
    elif user_action.startswith("complete"):
        try:
            ind = int(user_action[9:])
            ind = ind - 1

            todos = get_todos('tasks.txt')

            # when using readlines it adds a new line character at the end of each item in the list so we need to strip it before printing it to the user and before using it in the message to the user when we remove an item from the list
            todo_to_remove = todos[ind].strip('\n')
            todos.pop(ind)
            write_todos('tasks.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)


        except IndexError:
            print("there is no item with that number")
            continue
        
    elif user_action.startswith("exit"):
        break
    
    else:
        print("command is not valid")
    
print("bye!")   