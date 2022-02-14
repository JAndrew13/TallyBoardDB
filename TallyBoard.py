from tkinter import Tk, Button, Label, Scrollbar, Listbox, Checkbutton, StringVar, Entry, N, W,  E, S, END
from tkinter import ttk
from tkinter import messagebox


window = Tk()

window.title("Tally Board DB")
window.configure(background="orange")
window.geometry("400x600")
window.resizable(width=False, height=False)

# Main Window Init
title_label = ttk.Label(window, text="TallyBoard DB", background="orange", font=("TkDefaultFont", 16))
title_label.grid(row=1, column=1)
workers_label = ttk.Label(window, text="Available Workers", background="orange", font=("Ariel", 16))
workers_label.grid(row=2, column=1)

worker_button = ttk.Button(window, text="Worker 1")
worker_button.grid(row=3, column=1)


# INSERT DIVIDE LINE

add_work_button = ttk.Button(window, text="Add Work")
add_work_button.grid(row=4, column=1)
sub_work_button = ttk.Button(window, text="Sub Work")
sub_work_button.grid(row=4, column=2)

amount_5_btn = ttk.Button(window, text="5")
amount_5_btn.grid(row=5, column=1)
amount_10_btn = ttk.Button(window, text="10")
amount_10_btn.grid(row=5, column=2)
amount_25_btn = ttk.Button(window, text="25")
amount_25_btn.grid(row=5, column=3)
amount_50_btn = ttk.Button(window, text="50")
amount_50_btn.grid(row=5, column=4)
amount_100_btn = ttk.Button(window, text="100")
amount_100_btn.grid(row=6, column=1)
amount_200_btn = ttk.Button(window, text="200")
amount_200_btn.grid(row=6, column=2)
amount_400_btn = ttk.Button(window, text="400")
amount_400_btn.grid(row=6, column=3)
amount_800_btn = ttk.Button(window, text="800")
amount_800_btn.grid(row=6, column=4)

amount_custom_label = ttk.Label(window, text="custom amount -> ", font=("Ariel, 12"))
amount_custom_label.grid(row=7, column=1)
amount_custom = StringVar()
amount_custom_entry = ttk.Entry(window, width=24, textvariable=amount_custom)
amount_custom_entry.grid(row=7, column=2)

submit_button = ttk.Button(window, text="Submit")
submit_button.grid(row=8, column=2)

# INSERT DIVIDE LINE

edit_workers_button = ttk.Button(window,text="Edit Workers")
edit_workers_button.grid(row=9, column=1)
stats_button = ttk.Button(window, text="View Tallyboard")
stats_button.grid(row=9, column=2)

window.mainloop()
