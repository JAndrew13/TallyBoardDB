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

        employees_label = ttk.Label(self, background="Orange", text="Available Workers", font=FONT_BODY)
        employees_label.place(x=25 , y=100)

        self.WorkerDisplay(data)

        editEmp_btn = ttk.Button(self, text="Edit Employees",command=lambda: controller.show_frame(EditEmployees))
        editEmp_btn.place(x=25, y=550)
        viewTally_btn = ttk.Button(self,text="View Tally", command=lambda: controller.show_frame(Stats))
        viewTally_btn.place(x=300, y=550)

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

        custom_label = ttk.Label(text="Cust. Amount:", font=("Veranda", 8, "bold"), background="orange")
        custom_label.place(x=225, y=200)
        custom_entry = ttk.Entry(width=12)
        custom_entry.place(x=310, y=202)

        total_label = ttk.Label(text="Current Total:", font=("Veranda", 8, "bold"), background="orange")
        total_label.place(x=225, y=232)
        total_disp_label = ttk.Label(text="XXXX", font=("Veranda", 10, 'bold'), background="orange")
        total_disp_label.place(x=310, y=230)

        reset_button = ttk.Button(text="Reset Value", width= 25)
        reset_button.place(x=225, y=265)
        add_work_button = ttk.Button(self, text="Add Work")
        add_work_button.place(x= 225, y=300)
        sub_work_button = ttk.Button(self, text="Sub Work")
        sub_work_button.place(x= 310, y=300)

        # smiley = ttk.Label(text="😁😃😅😓😣😠", font=("Veranda", 18, "bold"), background="orange")
        # smiley.place(x=50, y=400)

# ================  TEMP DISPLAY  ========================
#     def WorkerTally(self):
        worker_name = "john"
        worker_tally = "2082"
        worker_mood = "😃"

        slot1 = ttk.Label(text=f"{worker_name} - ${worker_tally}",
                          font=("Veranda", 15, "bold"),
                          background='white')
        slot1.place(x=50, y=350)
        slot2 = ttk.Label(text=worker_mood, font=("Veranda", 18, "bold"), background="orange")
        slot2.place(x=15, y=345)


    def WorkerDisplay(self, worker_names):
        lb_workers = tk.Listbox(self, bd=3, font="Veranda", selectbackground="orange", height=13)
        lb_workers.place(x=15, y=70)
        for worker in worker_names:
            lb_workers.insert(END, worker)

class EditEmployees(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Edit Employees Page", font=FONT_BODY)
        label.grid(row=0, column=1)

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
