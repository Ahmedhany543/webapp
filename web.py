import streamlit as st
from functions import files_handle

todos = files_handle('r','')


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    files_handle('w', todos)


st.title("My To Do App")
st.subheader("This is my To Do List:")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        files_handle('w', todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="New To Do", placeholder="Add new todo...", on_change=add_todo, key='new_todo')

