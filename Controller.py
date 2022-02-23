from Model import Model, Workshop
from View import View
import operator

class Controller:

    # Startup Controller and initialize -> View, Model, Workshop
    def __init__(self):
        self.model = Model
        self.view = View(self)
        self.workshop = Workshop(self, self.model.load())
        self.submit = {"name": "", "amount": "", "oper": ""}

        # Initializes Application Data: Check for saved file / Creates New File
        # Loads Existing file -> Sets "Working Dictionary" as loaded file data

    def Initialize(self):

        # Check for existing database,  if non exists --> create database file
        print("checking database..")
        if self.model.checker():
            print("Success!")

        # Load Existing database
        data = self.model.load()
        print("Success!")

        # Gets data from Model(load) and sets Controller's "Working data"
        self.set_working_data(data)
        # Updates View's Entry Boxes
        self.update_entry_boxes()
        # Builds, Sorts, and Updates Worker Display
        self.view.update_long_data()

    # Takes new data (dict) -> Updates Controller's "Working Data" (dict)
    def set_working_data(self, new_data):
        self.working_data = new_data

    # Grab Data from Database and save to a usable dictionary
    def fetch_working_data(self):
        data = self.working_data
        return data

    def request_save(self):
        data = self.working_data
        self.model.save(data)

    # Grabs working data and returns a list of names
    def fetch_worker_names(self):
        worker_names = []
        for name in self.fetch_working_data():
            worker_names.append(name)
        return(worker_names)

    # Gets button-click input from View -> Decodes -> send to Response operator
    def action_button(self, button_text):
        print(f'action item: {button_text} clicked')
        response = self.model.decoder(self, button_text)

        self.response_operator(response=response)

    # Takes input code from Action Button -> directs relevant action
    def response_operator(self, response):
        # ADD
        if response == 1:
            Model.current_operand = Model.OPERANDS[1]
            self.submit["oper"] = "+"

        # SUBTRACT
        elif response == 2:
            Model.current_operand = Model.OPERANDS[2]
            self.submit["oper"] = "-"

        # ADD WORKER
        elif response == 3:
            if len(self.view.name_var.get())>0:
                name = self.view.name_var.get()
                self.set_working_data(self.workshop.add_worker(name))
                self.view.update_long_data()
            else:
                print("Error: No name entered")
                pass

        # DELETE WORKERS
        elif response == 4:
            if len(self.fetch_worker_names())>0:
                worker_name = self.get_selected_worker()
                self.set_working_data(self.workshop.del_worker(worker_name))
                self.view.update_long_data()
            else:
                print("Error: No workers to delete!")
                pass

        # SUBMIT TOTAL
        elif response == 6:

            name = self.get_selected_worker()
            if self.submit["oper"] == "+":
                amount = int(self.view.total_var.get().replace("+", ""))
                self.set_working_data(self.workshop.add_tally(name, amount))
            elif self.submit["oper"] == "-":
                amount = int(self.view.total_var.get().replace("-", ""))
                self.set_working_data(self.workshop.sub_tally(name, amount))

            self.view.update_long_data()

        # CLEAR TOTAL (DONE)
        elif response == 7:
            self.model.reset_total(self)
            self.view.cust_var.set("")

        self.update_entry_boxes()

    # Gets current total from View -> returns updated amount to View
    def get_total(self, custom_int):
        value  = Model.current_total
        oper = Model.current_operand
        if len(custom_int)>0:
            custom_int = int(custom_int)
            Model.current_total = (value + custom_int)
            print("TEST" + Model.current_total.get())
            return f"{oper}{value+custom_int}"
        else:
            return f"{oper}{value}"

    # Gets selected worker from view.listbox -> returns name of 'Selected Worker'
    def get_selected_worker(self):
        lb_index = self.view.listbox.curselection()
        return self.view.listbox.get(lb_index)

    # Updates View(Entry boxes) with current data
    def update_entry_boxes(self):
        self.view.update_short_data()

    # Takes Controllers "Working Data" (dict) -> Returns sorted dict(descending)
    def tally_sort(self, data):
        data_desc =sorted(data.items(), key=operator.itemgetter(1),reverse=True)
        sorted_workers = {}
        for item in data_desc:
            name = item[0]
            tally = item[1]
            sorted_workers[name] = tally
        return sorted_workers

    # Initialize View's mainloop()
    def main(self):
        self.view.main()

if __name__ == "__main__":

    Tallyboard = Controller()
    Tallyboard.Initialize()
    Tallyboard.main()




# ===================  Testing  =================== #

