def get_todos(filename='todo.txt'):
    """This is a DocString:
    This is read todos function
    to open a file in read mode and
    returns todos list"""
    with open(filename, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filename='todo.txt'):
    """This is write todos function
    to make changes in a file"""
    with open(filename, 'w') as file:
        file.writelines(todos)

print(__name__)
if __name__ == '__main__':
    print(help(get_todos))
    print("hello")
    '''when we use main function then if this file gets imported then above print code is not executed, it is only executed when this file is executed'''