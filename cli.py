from modules.functions import get_todos, write_todos
import time

now = time.strftime("%b %d - %Y, %H :%M :%S ")

while True:

    # Get user action and make it strip
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # ADD FUNCTION

    if user_action.startswith("add"):
        '''
        if user_action == 'add':
            plan = input("Enter your Todo: ")
            todo = plan

        else:
        '''
        todo = user_action[4:]      # making to enter space

        todos = get_todos()  # '' is argument value
        todos.append(f"{todo} --- Recorded at [{now}]" + "\n")

        '''
        file = open('files/subfiles/todos.txt', 'w')  # open file object
        file.writelines(todos)
        file.close()
        '''
        write_todos(todos)


    # SHOW FUNCTION

    elif user_action.startswith("show"):
        todos = get_todos()

        '''
        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        
        '''
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            print(f"{index + 1} - {item}")

    # EDIT FUNCTION

    elif user_action.startswith("edit"):

        try:

            number = int(user_action[5:])

            # number = input("Number of the do list")

            todos = get_todos()

            new_todo = input("Enter a new todo: ")
            todos[int(number) - 1] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("Your command is not vaild...")
            continue

    # COMPLETE FUNCTION

    elif user_action.startswith("complete"):
        try:

            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"Todo < {todo_to_remove} > was removed from the list..."
            print(message)

        except IndexError:
            print("Your command is not vaild...")
            continue

    # EXIT FUNCTION

    elif user_action.startswith("exit"):
        break

    else:
        print("Wrong command!!")


print('Good luck for you!!')
