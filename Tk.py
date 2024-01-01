import tkinter
from tkinter import messagebox

def change_color(color):
    window.configure(bg=color)

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")
        
def edit_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        selected_task = listbox_tasks.get(selected_task_index)
        entry_task.delete(0, tkinter.END)
        entry_task.insert(tkinter.END, selected_task)
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:   
        messagebox.showwarning("Warning", "Please select a task to delete.")

window = tkinter.Tk()
window.title("TO DO LIST")
window.configure(bg="black")
label = tkinter.Label(window, text ="   DO YOUR OWN LIST   ", font=("Arial Bold", 30), bg="pink", fg="black").pack()
window.geometry('350x350')

frame_tasks = tkinter.Frame(window)
frame_tasks.pack(pady=10)

listbox_tasks = tkinter.Listbox(frame_tasks, height=26, width=200, border=5, bg="Pink", fg="black")
listbox_tasks.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(window, width=200, border=5, bg="Pink", fg="black")
entry_task.pack(pady=10)

button_add_task = tkinter.Button(window, text="ADD", font=("Arial Bold", 15), width=100, bg="black", fg="pink", command=add_task)
button_add_task.pack()

button_edit_task = tkinter.Button(window, text="EDIT", font=("Arial Bold", 15), width=100, bg="black", fg="pink", command=edit_task)
button_edit_task.pack()

button_delete_task = tkinter.Button(window, text="DELETE", font=("Arial Bold", 15), width=100, bg="black", fg="pink", command=delete_task)
button_delete_task.pack()

window.mainloop()
