import tkinter as tk
import pandas as pd
from ttkwidgets.autocomplete import AutocompleteEntry

# Create the main window
root = tk.Tk()

options = pd.read_csv('test_data.csv').iloc[:, 0].tolist() 

current_test_case = []

def clear_menu(): #this will completely clear the GUI menu
    for widget in root.winfo_children():
        widget.destroy()

def add_test_step(autocomplete_widget, x_pos, y_pos):
    global current_test_case
    for step in current_test_case:
        print(step)
    current_test_case.append(autocomplete_widget.get())
    list_text = "\n".join(current_test_case)
    label = tk.Label(root, text=list_text, justify="left")
    label.place(x=x_pos,y=y_pos)
    print(autocomplete_widget.get())

def display_list_in_label(item_list, x, y):
    list_text = "\n".join(item_list)
    label = tk.Label(root, text=list_text, justify="left")
    label.place(x=x,y=y)

def display_main_menu():
    clear_menu()
    root.title("Testing Buddy")
    root.geometry("345x200")
    combobox = AutocompleteEntry(root, completevalues=options)
    combobox.place(x=5)
    add_step_button = tk.Button(root, text = "Add Step", command = lambda:add_test_step(combobox, 200, 50))
    add_step_button.place(x=200)


def run_gui():
    display_main_menu()
    root.mainloop()

# Run the Tkinter event loop
run_gui()