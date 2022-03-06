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
    FONT_FROZEN_LG = ("Veranda", 14, "bold")
    FONT_FROZEN_BOLD = ("Veranda", 12, "bold")

    # Colors
    FRAME_TEST = "blue"
    BG_COLOR = "orange2"
    UNFROZEN_COL = "skyblue"
    FROZEN_COL = "tomato1"


    # Main View Class
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.last_selection = ""

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

    # Creates master widget container in view
    def _make_main_frame(self):

        self._container = tk.Frame(self, background=self.BG_COLOR)
        self._container.pack(side="top", fill="both", expand=True, padx=self.PAD, pady=self.PAD)

    # Creates the listbox object of selectable workers
    def _make_worker_selector(self, workers):
        selection = 0

        frm = ttk.Frame(self._container)
        frm.place(x=10, y=50)

        self.workers = workers
        self.lb_workers = tk.Listbox(frm, bd=3, font=self.FONT_BOLD, activestyle='dotbox', selectbackground=self.BG_COLOR, height=10)
        self.lb_workers.pack()

        for worker in self.workers:
            self.lb_workers.insert(END, worker)
        self.listbox = self.lb_workers

        self.listbox.selection_anchor(selection)
        self.listbox.select_set(tk.ANCHOR, selection)

# =================== Widget and View creation ===================== #

    # Creates the majority of widgets on screen
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

    # A Button creation factory..
    def _button_factory(self, container, text, width, side, button_name):
        btn = ttk.Button(container, text=text, width=width, command=
                         lambda button=button_name: self.controller.action_button(button_name))
        btn.pack(side=side, padx=2, pady=2)

    # adds ON / OFF funtionality to operand buttons
    def _button_add(self):
        self.btn_adder.config(state=tk.DISABLED)
        self.btn_subber.config(state=tk.ACTIVE)

    # adds ON / OFF funtionality to operand buttons
    def _button_sub(self):
        self.btn_adder.config(state=tk.ACTIVE)
        self.btn_subber.config(state=tk.DISABLED)

    # Resets the state of ADD / SUB operand buttons
    def _button_reseter(self):
        self.btn_adder.config(state=tk.ACTIVE)
        self.btn_subber.config(state=tk.ACTIVE)

    # Creates active display of Workers and their data
    def _display_factory(self, name, tally, status):
        if status == "freeze":
            color = self.UNFROZEN_COL
        else:
            color = self.FROZEN_COL

    # Create inner frame for worker display widgets
        self.row_frame = tk.Frame(self.worker_outer_frame, height=25, width=365, background=self.BG_COLOR, )
        self.row_frame.pack(side="top")
    # Worker Name
        name_lbl = ttk.Label(self.row_frame, text=name, font=self.FONT_BOLD, background=self.BG_COLOR, anchor='w', width=10)
        name_lbl.pack(side='left', padx=2, pady=3)
    # Worker Tally
        tally_lbl = ttk.Label(self.row_frame, text=tally, font=self.FONT_TITLE, background=self.BG_COLOR, anchor='w', width=8)
        tally_lbl.pack(side='left', padx=6, pady=2)
    # Worker Tally Reset
        reset_btn = ttk.Button(self.row_frame, text='reset', width=13, command=lambda: self.controller.clear_individual_tally(name, tally))
        reset_btn.pack(side='left', pady=2)
    # Worker Freeze
        self.freeze_btn = tk.Button(self.row_frame, text=status, width=9, bg=color, command=lambda: self.freeze_worker(name, tally))
        self.freeze_btn.pack(side='left', padx=4, pady=2)

    # Arranges all of the workers in the lower display
    def _make_worker_display(self, workers):
        # Create outer frame for worker data display
        self.worker_outer_frame = \
            tk.Frame(self._container, width=365, height=265, background=self.BG_COLOR)
        self.worker_outer_frame.place(x=10, y=270)

        # Get all workers and pass through ascending sorter
        sorted_workers = self.controller.tally_sort()

        unfrozen = 'freeze'
        frozen = 'unfreeze'

        for worker in sorted_workers:
            name = worker
            tally = sorted_workers[worker]
            if name in self.controller.config.frozen:
                status = frozen
            else:
                status = unfrozen
            self._display_factory(name, tally, status)

    # Controls response from workers "freeze" buttons
    def freeze_worker(self, name, tally):
        # if the worker is already frozen, then unfreeze
        if name in self.controller.frozen_workers:
            self.controller.config.del_frozen(name)
            self.controller.frozen_workers.pop(name)

        else:
            # config save frozen worker name
            self.controller.config.add_frozen(name)
            # add worker name to controllers frozen list
            self.controller.frozen_workers[name] = int(tally)

        # Sort worker display list with new data
        self.controller.tally_sort()

        # refresh view (update long data)
        self.controller.update_view()


# ================== Entry Box text Validators =================== #
    # Only allows numbers to be entered
    def _only_numbers(self, char):
            return char.isdigit()

    # Only allows letters to be entered
    def _only_letters(self, char):
            return char.isalpha()

# =================== "Custom Number" entry functions =================== #
    # gets value entered in the custom number entry box
    def _get_cust_var(self):
        return self.cust_var.get()

    # sets the custom entry amount to temporary data
    def _set_cust_var(self, value):
        self.cust_var.set(value)

# ================== Data Updating Functions =================== #

    # Updates shorthand data (Value display labels)
    # Used to update, show, and save changes to worker totals ie. Submit, reset, clear
    def update_short_data(self):
        # pull new "temporary" total from controller -> send to display label
        self.worker_outer_frame.destroy()
        self._make_worker_display(workers=self.controller.fetch_working_data())

        # Send database save request to controller
        self.controller.request_save()

    # Updates long term data values (worker selector and lower display) -> sends save request to controller
    # Used to Add / Delete workers from workshop
    def update_long_data(self):

        # Update worker selector screen
        self._make_worker_selector(workers=self.controller.fetch_worker_names())

        # Update lower display for worker information
        self.worker_outer_frame.destroy()
        self._make_worker_display(workers=self.controller.fetch_worker_names())

        # Send database save request to controller
        self.controller.request_save()

    # Initializes the Worker's Selector box and Display
    def initialize_view(self):
        # Sort worker display list with new data
        self._make_worker_selector(workers=self.controller.fetch_worker_names())
        self._make_worker_display(workers=self.controller.fetch_worker_names())
        self._set_bg_color()

# =================== App Modifiers ======================== #
    # sets View's Default BG Color
    def _set_bg_color(self):
        if self.BG_COLOR == self.controller.current_color:
            self.set_new_color(self.controller.current_color)
        else:
            new_color = self.controller.fetch_bg_color()
            print(new_color)
            self.set_new_color(new_color)

    def set_new_color(self, new_color):
        self.configure(bg=new_color)
        self.BG_COLOR = new_color
        self._container.destroy()
        self._make_main_frame()
        self._make_widgets()
        self.update_long_data()

    # opens color picker window
    def color_change(self):
        new_color=(askcolor(title="Tkinter Color Chooser")[1])
        self.set_new_color(new_color)
        self.controller.config.set_bg(f"{new_color}")

    def main(self):
        self.mainloop()