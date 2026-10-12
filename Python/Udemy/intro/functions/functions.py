def get_todos(filepath):
    """Reads the list of todos from a file and returns it."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    """Writes the list of todos to a file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


print(__name__)

if __name__ == "__main__":
    print("hello")
    print(get_todos())