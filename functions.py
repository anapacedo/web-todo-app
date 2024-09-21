FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Reads a text file and
    returns a list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write to-do items
    in a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == '__main__':
    print("testing main conditionals")
    # __name__ is main only when I run this file
