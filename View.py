import tkinter as tk
from tkinter import ttk, END, W
from tkinter.colorchooser import askcolor


class View(tk.Tk):

    # Class Variables
    WINDOW_SIZE = "400x600"

    # Window Padding
    PAD = 10

    # Button Factory Variables
    BUTTONS_ROW_COUNT = 3
    button_captions = [1, 5, 10, 25, 50, 100, 250, 500, 1000,]

    # Worker Display Factory Variables
    WORKERS_ROW_COUNT = 1


    # Window Styling Variables
    FONT_BODY = ("Veranda", 12)
    FONT_BOLD = ("Veranda", 12, "bold")
    FONT_TITLE = ("Veranda", 14, "bold")
    FONT_SMALL = ("Veranda", 8, "bold")

    FRAME_TEST = "blue"
    BG_COLOR = "Orange2"

    # Main View Class
    def __init__(self, controller):
        super().__init__()

        self.controller = controller


    # Main window properties

        tk.Tk.iconbitmap(self, default="tallyicon.ico")
        self.title("Tally Board DB")
        tk.Tk.wm_geometry(self, self.WINDOW_SIZE)
        tk.Tk.wm_resizable(self, width=False, height=False)
        tk.Tk.configure(self, background=self.BG_COLOR)


        self.cust_var = tk.IntVar()
        self.name_var = tk.StringVar()

        self._make_main_frame()
        self._make_widgets()
        self.current_total = 0

        self.update_short_data()


    # Creates master widget container in view
    def _make_main_frame(self):
        self._container = tk.Frame(self, background=self.BG_COLOR)
        self._container.pack(side="top", fill="both", expand=True, padx=self.PAD, pady=self.PAD)

    def _make_worker_selector(self, workers):
        frm = ttk.Frame(self._container)
        frm.place(x=10, y=50)

        self.workers = workers
        self.lb_workers = tk.Listbox(frm, bd=3, font=self.FONT_BOLD, activestyle='dotbox', selectbackground=self.BG_COLOR, height=10)
        self.lb_workers.pack()

        for worker in self.workers:
            self.lb_workers.insert(END, worker)
        self.listbox = self.lb_workers
        self.listbox.selection_anchor(0)
        self.listbox.select_set(tk.ANCHOR, 0)

# =================== Widget and View creation ===================== #

    def _make_widgets(self):
    # Frame : Button Grid
        outer_frm = tk.Frame(self._container)
        outer_frm.place(x=210, y=50)
        frm = tk.Frame(outer_frm, background=self.BG_COLOR)
        frm.pack()

        buttons_in_row = 0

    # Button Grid Factory
        for button_text in self.button_captions:
            if buttons_in_row == self.BUTTONS_ROW_COUNT:
                frm = tk.Frame(outer_frm, background=self.BG_COLOR)
                frm.pack()
                buttons_in_row = 0

            btn = ttk.Button(frm, text=button_text, width=7, command=(lambda button=f"INT-{button_text}": self.controller.action_button(button)))
            btn.pack(side='left', padx=2, pady=2)
            buttons_in_row += 1


    # Frame : Custom integer amount
        self.cust_frm = tk.Frame(self._container, background=self.BG_COLOR)
        self.cust_frm.place(x=210, y=145)
        self.validation = self.cust_frm.register(self._only_numbers)
        # Label : Custom Description
        self.lbl_total = tk.Label(self.cust_frm, text="Total:", font=(self.FONT_BOLD), background=self.BG_COLOR)
        self.lbl_total.pack(side='left', padx=2, pady=2)


        # Entry : Custom Amount
        self.ent_custom = ttk.Entry(self.cust_frm,
                                    validate="key",
                                    validatecommand=(self.validation, '%S', ),
                                    justify="right",
                                    textvariable=self.cust_var,
                                    width=12,
                                    font=(self.FONT_BOLD)
                                    )
        self.ent_custom.pack()


    # Frame : Operators
        operator_frm = tk.Frame(self._container, background=self.BG_COLOR)
        operator_frm.place(x=210, y=200)
    # Button : Add
        self.btn_adder = ttk.Button(operator_frm, text="Add ( + )", width=13, command=lambda: self.controller.action_button("ADD"))
        self.btn_adder.pack(side='left', padx=2, pady=2)
    # Button : Subtract
        self.btn_subber = ttk.Button(operator_frm, text="Sub ( - )", width=10, command=lambda: self.controller.action_button("SUB"))
        self.btn_subber.pack(side='left', padx=2, pady=2)



    # Create submit and reset buttons

    # Frame : Conformations
        conf_frm = tk.Frame(self._container, background=self.BG_COLOR)
        conf_frm.place(x=210, y=230)
    # Button : Submit Total
        self._button_factory(conf_frm, "Submit", 13, 'left', button_name="SubmitTotal")
    # Button : Reset Value Total
        self._button_factory(conf_frm, "Reset", 10, 'left', button_name="ResetTotal")


    # Create Database Mod Buttons

    # Frame : Database Mods
        mod_frm = tk.Frame(self._container, background=self.BG_COLOR)
        mod_frm.place(x=10,y=15)

    # Button : Delete Worker
        self._button_factory(mod_frm, "Del Worker.", 13, 'left', button_name="DeleteWorker")
    # Button : Add Worker
        self._button_factory(mod_frm, "AddWorker", 13, 'left', button_name="AddWorker")
    # Entry : Worker Name Entry
        self.validation_alpha = self.cust_frm.register(self._only_letters)
        name_entry = ttk.Entry(mod_frm,
                               validate="key",
                               validatecommand=(self.validation_alpha, '%S'),
                               justify="left",
                               textvariable=self.name_var,
                               width=27,
                               font=self.FONT_BOLD)
        name_entry.pack(side='right', padx=16)

    # Create settings Buttons
        self.settings_frm = tk.Frame(self._container, background=self.BG_COLOR)
        self.settings_frm.place(x=308, y=550)

    # Button : Color Picker =
        self.clr_btn = ttk.Button(self.settings_frm, text="Color Picker",  command=lambda: self.color_change())
        self.clr_btn.pack()

    def _button_factory(self, container, text, width, side, button_name, *args,**kwargs):
        btn = ttk.Button(container, text=text, width=width, command=
                         lambda button=button_name: self.controller.action_button(button_name))
        btn.pack(side=side, padx=2, pady=2)

    def _button_add(self):
        self.btn_adder.config(state=tk.DISABLED)
        self.btn_subber.config(state=tk.ACTIVE)

    def _button_sub(self):
        self.btn_adder.config(state=tk.ACTIVE)
        self.btn_subber.config(state=tk.DISABLED)

    def _button_reseter(self):
        self.btn_adder.config(state=tk.ACTIVE)
        self.btn_suber.config(state=tk.ACTIVE)
    def _make_worker_display(self, workers):
        # Create outer frame for worker data display
        outer_frame = tk.Frame(self._container, width=360, height=300,
                               highlightthickness=3,
                               highlightbackground=self.BG_COLOR,
                               background=self.BG_COLOR)
        outer_frame.place(x=10, y=270)

        # Create inner frame for worker displays
        inner_frame = tk.Frame(outer_frame, background=self.BG_COLOR)
        inner_frame.pack()

        # worker counter
        self.workers_in_row = 0

        # sort workers by Tally amount
        sorted_workers = self.controller.tally_sort()
        #worker display iterator
        print(sorted_workers)
        for worker in sorted_workers:

            if self.workers_in_row == self.WORKERS_ROW_COUNT:
                inner_frame = tk.Frame(outer_frame, background=self.BG_COLOR, highlightthickness=0)
                inner_frame.pack()

                self.workers_in_row = 0

            name_lbl = ttk.Label(inner_frame, text=worker, font=self.FONT_BOLD, background=self.BG_COLOR, anchor='w', width=8)
            name_lbl.pack(side='left', padx=2, pady=5)
            tally_lbl = ttk.Label(inner_frame,text=f"${workers[worker]}", font=self.FONT_TITLE, background=self.BG_COLOR, anchor='w', width=8)
            tally_lbl.pack(side='left', padx=2, pady=2)
            temp_lbl = ttk.Label(inner_frame, text=f"{self.controller.get_mood(workers[worker])}",font=self.FONT_TITLE, background=self.BG_COLOR, anchor='w', width=8)
            temp_lbl.pack(side='left', padx=2, pady=2)

            self.workers_in_row += 1

# ================== Entry Box text Validators =================== #

    def _only_numbers(self, char):
            return char.isdigit()

    def _only_letters(self, char):
            return char.isalpha()

# =================== Custom Entry Variale Functions =================== #

    def _get_cust_var(self):
        print("returning custom var")
        return self.cust_var.get()

    def _set_cust_var(self, value):
        print("Setting custom var entry")
        self.cust_var.set(value)

# ================== Data Updating Functions =================== #

    # Updates shorthand data (Value display labels)
    def update_short_data(self):
        # pull new "temporary" total from controller -> send to display label
        pass

    # Updates long term data values (worker selector and lower display) -> sends save request to controller
    def update_long_data(self):
        # Update worker selector screen
        self._make_worker_selector(workers=self.controller.fetch_worker_names())
        # Update lower display for worker information
        self._make_worker_display(workers=self.controller.fetch_working_data())
        # Send database save request to controller
        self.controller.request_save()

    def reset_view(self):
        pass

    def initialize_view(self):
        self._make_worker_selector(workers=self.controller.fetch_worker_names())
        self._make_worker_display(workers=self.controller.fetch_working_data())

    def color_change(self):
        new_color=(askcolor(title="Tkinter Color Chooser"))
        self.BG_COLOR = new_color[1]
        self.reset_view()

    def main(self):
        self.mainloop()