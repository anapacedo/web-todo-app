import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo.title())
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my to-do app.")
st.write("I built it in Python.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Add new to-do:",
              on_change=add_todo,
              key='new_todo')


