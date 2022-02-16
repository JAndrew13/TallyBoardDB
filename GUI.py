import tkinter as tk
from tkinter import ttk

FONT_BODY = ("Veranda", 12)

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
        tk.Frame.__init__(self, parent)
        tk.Tk.configure(self, background="Orange")
        tk.Tk.grid_rowconfigure(self, 0, weight=0)
        tk.Tk.grid_columnconfigure(self, 0, weight=0)

        title_label = ttk.Label(self,background="Orange", text="~=Tally Board=~", font=FONT_BODY)
        title_label.grid(row=0, column=1)
        employees_label = ttk.Label(self, background="Orange", text="Available Workers", font=FONT_BODY)
        employees_label.grid(row=1, column=1, padx=10, pady=10)


        # INSERT DIVIDE LINE

        add_work_button = ttk.Checkbutton(self, text="Add Work")
        add_work_button.grid(row=4, column=1)
        sub_work_button = ttk.Checkbutton(self, text="Sub Work")
        sub_work_button.grid(row=4, column=2)

        # INSERT DIVIDE LINE

        editEmp_btn = ttk.Button(self, text="Edit Employees",command=lambda: controller.show_frame(EditEmployees))
        editEmp_btn.grid(row=10, column=0)
        viewTally_btn = ttk.Button(self,text="View Tally", command=lambda: controller.show_frame(Stats))
        viewTally_btn.grid(row=10, column=2)


    # def WorkerDisplay(self):
    #     total_workers = len(AvailableWorkers + 1)
    #     row = (total_workers/3)+2
    #     col = 0
    #
    #     for worker in AvailableWorkers:
    #         worker_button = ttk.Checkbutton(self, text=worker)
    #         worker_button.grid(row=row, column=col)


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
