import tkinter as tk

# window config
window = tk.Tk()
window.geometry("400x800")
window.title("Tech Note Generator")

# helper functions
def add_to_grid(widget, row, column):
    widget.grid(row=row, column=column)


# variables needed
pt_name = tk.StringVar(window) # used in pt_name_entry as text_variable
room_number = tk.StringVar(window) # used in room number list box

###################
###   WIDGETS   ###
###################
# patient name entry
w= tk.Label(window, text='Patient Name', font="80")
add_to_grid(w, 0, 0 )
pt_name_entry = tk.Entry(window, textvariable=pt_name)
add_to_grid(pt_name_entry, 0, 1)

# room number List box
rm_num_label = tk.Label(window, text="Room Number")
add_to_grid(rm_num_label, 1, 0)
rm_num = tk.Listbox(window)
rm_num.insert(1, "1")
rm_num.insert(2, "2")
rm_num.insert(3, "3")

add_to_grid(rm_num, 1, 1)


window.mainloop()
