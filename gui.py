# GUI means 'Graphical User Interface'

import modules.functions
import PySimpleGUI as sg
import time

sg.theme('GreenTan')

clock = sg.Text('', key="clock")
label = sg.Text("Type in a To-do:")
input_box = sg.InputText(tooltip="Enter Todo to record what you wanna do...", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=modules.functions.get_todos(), key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

output_label = sg.Text(key="output", text_color="red")

# The title of the window
"""
layout should have a list inside the list! Widgets...
"""

window = sg.Window('My To-do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, output_label]],
                   font=('Lucid', 15))

while True:

    user_action, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d - %Y, %H:%M:%S") + "       Made by Wenzhe")

    match user_action:
        case "Add":
            todos = modules.functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)

            modules.functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values['todo']

                todos = modules.functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                modules.functions.write_todos(todos)

                window['todos'].update(values=todos)  # update is part of listbox

            except IndexError:
                window["output"].update(value="Please select an item first!!")
                # or using PySimpleGUI.popup

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = modules.functions.get_todos()
                todos.remove(todo_to_complete)
                modules.functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')

            except IndexError:
                window["output"].update(value="Please select an item first!!")

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
