# GUI means 'Graphical User Interface'

import modules.functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-do:")
input_box = sg.InputText(tooltip="Enter Todo to record what you wanna do...")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label], [input_box, add_button]])  # The title of the window
window.read()
window.close()