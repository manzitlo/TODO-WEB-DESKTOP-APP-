FILENAME = 'files/subfiles/todos.txt'

def get_todos(filepath=FILENAME):  # filepath is parameter
    """
    file = open('files/subfiles/todos.txt', 'r')
    todos = file.readlines()  # create the list, the same like []
    file.close()
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILENAME):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":  # __name__ is string
    print("Hello from functions")

""" __name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被运行。"""