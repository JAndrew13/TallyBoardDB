import tkinter as tk
from tkinter import ttk, messagebox, Listbox, END
import Manager

FONT_BODY = ("Helvetica", 12, "bold")

class TallyBoardDB(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self, default="image.ico")
        tk.Tk.wm_title(self, "Tally Board DB")
        tk.Tk.wm_geometry(self, "400x600")
        tk.Tk.wm_resizable(self, width=False, height=False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, EditEmployees, Stats):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        data = [name for name in Manager.Db.db_pull(self)]

        tk.Frame.__init__(self, parent)
        tk.Tk.configure(self, background="Orange")

        spacer1 = tk.Label(self, text="", )
        spacer1.grid(row=0, column=0)

        employees_label = ttk.Label(self, background="Orange", text="Available Workers", font=FONT_BODY)
        employees_label.grid(row=1, column=0)

        self.WorkerDisplay(data)

        # INSERT DIVIDE LINE

        spacer2 = tk.Label(self, text="")
        spacer2.grid(row=0, column=2,)
        spacer3 = tk.Label(self, text="")
        spacer3.grid(row=1, column=2, )

        # INSERT DIVIDE LINE

        editEmp_btn = ttk.Button(self, text="Edit Employees",command=lambda: controller.show_frame(EditEmployees))
        editEmp_btn.grid(row=4, column=0)
        viewTally_btn = ttk.Button(self,text="View Tally", command=lambda: controller.show_frame(Stats))
        viewTally_btn.grid(row=5, column=0)

        amount_5_btn = ttk.Button(self, text="5")
        amount_5_btn.place(x= 225, y=70)
        amount_10_btn = ttk.Button(self, text="10")
        amount_10_btn.place(x= 310, y=70)
        amount_25_btn = ttk.Button(self, text="25")
        amount_25_btn.place(x= 225, y=103)
        amount_50_btn = ttk.Button(self, text="50")
        amount_50_btn.place(x= 310, y=103)
        amount_100_btn = ttk.Button(self, text="100")
        amount_100_btn.place(x= 225, y=136)
        amount_200_btn = ttk.Button(self, text="200")
        amount_200_btn.place(x= 310, y=136)
        amount_400_btn = ttk.Button(self, text="400")
        amount_400_btn.place(x= 225, y=169)
        amount_800_btn = ttk.Button(self, text="800")
        amount_800_btn.place(x= 310, y=169)

        add_work_button = ttk.Button(self, text="Add Work")
        add_work_button.place(x= 225, y=220)
        sub_work_button = ttk.Button(self, text="Sub Work")
        sub_work_button.place(x= 310, y=220)
    def WorkerDisplay(self, data):
        lb_workers = tk.Listbox(self, bd=4, font="Veranda", selectbackground="orange")
        lb_workers.grid(row=3, column=0, padx=20, pady=20 )
        for worker in data:
            lb_workers.insert(END, worker)




class EditEmployees(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Edit Employees Page", font=FONT_BODY)
        label.grid(row=0, column=1 )

        return_btn = ttk.Button(self, text='Return to Main', width=25, command=lambda: controller.show_frame(StartPage))
        return_btn.grid(row=10, column=1)

class Stats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tally Board : Stats", font=FONT_BODY)
        label.grid(row=1, column=1, rowspan=2)
        button1 = ttk.Button(self, text='Return to Main', width=25,
                        command=lambda: controller.show_frame(StartPage))
        button1.grid(row=10, column=1)
