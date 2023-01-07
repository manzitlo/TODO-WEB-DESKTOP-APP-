# GUI means 'Graphical User Interface'

import modules.functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do:")
input_box = sg.InputText(tooltip="Enter Todo to record what you wanna do...", key="todo")
add_button = sg.Button("Add")

# The title of the window
"""
layout should have a list inside the list! Widgets...
"""

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Hsafdhafhlaf', 15))

while True:
    user_action, values = window.read()

    print(user_action)
    todo = values
    print(todo)

    match user_action:
        case "Add":
            todos = modules.functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)

            modules.functions.write_todos(todos)

        case sg.WIN_CLOSED:
            break

window.close()
