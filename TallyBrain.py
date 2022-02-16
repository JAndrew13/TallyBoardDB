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
        label = ttk.Label(self,background="Orange", text="Welcome to Tally Board!", font=FONT_BODY)
        label.pack(pady=10,padx=10)

        editEmp_btn = ttk.Button(self, text="Edit Employees",command=lambda: controller.show_frame(EditEmployees))
        editEmp_btn.pack()

        viewTally_btn = ttk.Button(self,text="View Tally", command=lambda: controller.show_frame(Stats))
        viewTally_btn.pack()


class EditEmployees(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Edit Employees Page", font=FONT_BODY)
        label.pack(padx=10, pady=10)

        return_btn = ttk.Button(self, text='Return to Main', width=25, command=lambda: controller.show_frame(StartPage))
        return_btn.pack()

class Stats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tally Board : Stats", font=FONT_BODY)
        label.pack(padx=10, pady=10)
        button1 = ttk.Button(self, text='Return to Main', width=25,
                        command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = TallyBoardDB()
app.mainloop()