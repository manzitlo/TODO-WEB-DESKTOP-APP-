import streamlit as st

import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    print(new_todo)
    todos.append(new_todo)
    functions.write_todos(todos)


st.subheader("This is my first Web-App!")
st.write("Using this App to increase your <b>productivity</b>...",
         unsafe_allow_html=True)     # HTML language will be allowed.

st.title("My TODO List APP")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo at your list...",
              on_change=add_todo, key='new_todo')
