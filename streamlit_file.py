import streamlit as st
import functions

todos = functions.get_todos()

def get_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""

st.title("My Todo App")
st.subheader("This app can add, edit, delete from to-do list")

st.text_input(label="", placeholder="Add a todo", on_change=get_todo, key='new_todo')

with open('todo.txt', 'r') as file:
    file.readlines()

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{todo}_{index}"]
        st.experimental_rerun()

print(st.session_state['new_todo'])
# for i in
# st.checkbox("check")
# st.checkbox("check2")