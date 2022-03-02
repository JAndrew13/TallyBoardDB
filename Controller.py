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
        self.frozen_workers = {}


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
        # Set current_total to 0
        self.model.current_total = 0
        # Initializes startup view
        self.view.initialize_view()

    # Takes new data (dict) -> Updates Controller's "Working Data" (dict)
    def set_working_data(self, new_data):
        self.working_data = new_data

    # Grab Data from Database and save to a usable dictionary
    def fetch_working_data(self):
        data = self.working_data
        return data

    # pull working data and request DB save via Model
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
        if "INT" in button_text:
            new_total = self._get_int(button_text)
            print(new_total)
            self.get_set_current_total()
            response = 5
            self.response_operator(response=response)
        else:
            response = Model.decoder(self, code=button_text)
            self.response_operator(response=response)

        # reset view
        self.view.update_long_data()

    # Gets integer from button code
    def _get_int(self, code):
        int_test = [item for item in code.split("-")]
        int_val = int_test[1]
        response = 5
        custom_value = self.view._get_cust_var()
        total_value = custom_value + int(int_val)
        self.model.current_total = total_value

        return response

    # Takes input code from Action Button -> directs relevant action
    def response_operator(self, response):
        # ADD
        if response == 1:
            Model.current_operand = Model.OPERANDS[1]
            self.submit["oper"] = "+"
            self.view._button_add()

        # SUBTRACT
        elif response == 2:
            Model.current_operand = Model.OPERANDS[2]
            self.submit["oper"] = "-"
            self.view._button_sub()

        # ADD WORKER
        elif response == 3:
            if len(self.view.name_var.get())>0:
                name = self.view.name_var.get()
                self.set_working_data(self.workshop.add_worker(name))
                self.view.worker_outer_frame.destroy()
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

        # ADD CURRENT TOTAL
        elif response == 5:
            self.get_set_current_total()

        # SUBMIT TOTAL
        elif response == 6:

            name = self.get_selected_worker()
            if self.submit["oper"] == "+":
                amount = int(self.view.cust_var.get())
                self.set_working_data(self.workshop.add_tally(name, amount))
            elif self.submit["oper"] == "-":
                amount = int(self.view.cust_var.get())
                self.set_working_data(self.workshop.sub_tally(name, amount))

            self.view.update_short_data()
            self.view._button_reseter()

        # CLEAR TOTAL (DONE)
        elif response == 7:
            Model.reset_total(self)
            self.view.cust_var.set(0)
            self.view._button_reseter()
            self.submit["oper"] = ""

    # Gets current total from Model -> return current total integer
    def get_current_total(self):
        return self.model.current_total

    def get_set_current_total(self):
        self.view._set_cust_var(self.model.current_total)

    def get_operand(self):
        return self.submit["oper"]

    # Gets selected worker from view.listbox -> returns name of 'Selected Worker'
    def get_selected_worker(self):
        return self.view.listbox.get(self.view.listbox.curselection())

    # Takes Workers tally value as input -> returns mood emoji
    def get_mood(self, amount):

        # if worker amount = 0, return basic mood
        if amount == 0:
            return self.model.MOOD_ICONS[0]
        index = 0

        # iterate through mood scale and compare value to worker tally
        for bracket in self.model.MOOD_SCALE:

            # if amount is more than mood scale value, test next bracket
            if amount >= bracket:
                index += 1

            # if amount is less than mood scale value, get index and return emoji
            else:
                return self.model.MOOD_ICONS[index]

    # Takes Controllers "Working Data" (dict) -> Returns sorted dict(descending)
    def tally_sort(self):
        data_desc = sorted(self.working_data.items(), key=operator.itemgetter(1),reverse=True)
        sorted_workers = {}

        for item in data_desc:
            if item[0] in self.frozen_workers:
                pass
            else:
                sorted_workers[item[0]] = item[1]
        for item in data_desc:
            if item[0] not in sorted_workers:
                sorted_workers[item[0]] = item[1]
            else:
                pass
        return sorted_workers

    # Initialize View's mainloop()
    def main(self):
        self.view.main()

if __name__ == "__main__":

    Tallyboard = Controller()
    Tallyboard.Initialize()
    Tallyboard.main()




# ===================  Testing  =================== #

