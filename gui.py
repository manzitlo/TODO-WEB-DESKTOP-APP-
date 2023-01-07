# GUI means 'Graphical User Interface'

import modules.functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do:")
input_box = sg.InputText(tooltip="Enter Todo to record what you wanna do...", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=modules.functions.get_todos(), key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")

# The title of the window
"""
layout should have a list inside the list! Widgets...
"""

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))

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
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values['todo']

            todos = modules.functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            modules.functions.write_todos(todos)

            window['todos'].update(values=todos)  # update is part of listbox

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
