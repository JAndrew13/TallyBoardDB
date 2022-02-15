import tkinter as tk

FONT_BODY = ("Veranda", 12)


class TallyBoardDB(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
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
        label = tk.Label(self, text="Start Page", font=FONT_BODY)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="Edit Employees",
                            command=lambda: controller.show_frame(EditEmployees))
        button.pack()

        button2 = tk.Button(self, text="View Tally",
                            command=lambda: controller.show_frame(Stats))
        button2.pack()

class EditEmployees(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Edit Employees Page", font=FONT_BODY)
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text='Return to Main', width=25,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class Stats(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tally Board : Stats", font=FONT_BODY)
        label.pack(padx=10, pady=10)
        button1 = tk.Button(self, text='Return to Main', width=25,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = TallyBoardDB()
app.mainloop()