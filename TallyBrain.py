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

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(text="hello", font=FONT_BODY)
        button1 = tk.Button(text = 'Edit Employees', width = 25)
        button2 = tk.Button(text = 'View Tally', width=25)

        label.pack()
        button1.pack()
        button2.pack()

app = TallyBoardDB()
app.mainloop()