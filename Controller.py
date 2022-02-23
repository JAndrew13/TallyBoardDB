from Model import Model, Workshop
from View import View

class Controller:

    def __init__(self):
        self.model = Model
        self.view = View(self)


    def fetch_working_data(self):
        Model.WORKING_DB = self.model.load()
        print(f"Data from controller - init: {Model.WORKING_DB}")
        return Model.WORKING_DB

    def fetch_workers(self):
        worker_names = []
        for name in self.fetch_working_data():
            worker_names.append(name)
        return(worker_names)

    def action_button(self, button_text):
        print(f'action item: {button_text} clicked')
        response = self.model.decoder(self, button_text)

        self.response_operator(response=response)
        self.update_view()

    def response_operator(self, response):
        # ADD
        if response == 1:
            Model.current_operand = Model.OPERANDS[1]

        # SUBTRACT
        elif response == 2:
            Model.current_operand = Model.OPERANDS[2]

        # ADD WORKER
        elif response == 3:
            Model.create_worker(self, name="foo")
            # If the Name Entry has a name to add
            # if self.view.name_var.get():
            #     # name = self.view.name_var.get().lower()
            #     # self.view.lb_workers.insert(len(self.view.workers), name.capitalize())
            #     # print(True)
            # else:
            #     #NAME ERROR (no inputs)
            #     print(False)
            pass

        # DELETE WORKERS
        elif response == 4:

            # worker_name = self.get_selected_worker()
            # print(f"selected worker: {worker_name}")
            pass

        # SUBMIT TOTAL
        elif response == 6:
            pass

        # CLEAR TOTAL
        elif response == 7:
            self.model.reset_total(self)
            self.view.cust_var.set("")

        self.update_view()

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

    def get_selected_worker(self):
        lb_index = self.view.listbox.curselection()
        return self.view.listbox.get(lb_index)

    def update_view(self):
        self.view.update_data()

    def Initialize(self):

        # Check for existing database,  if non exists --> create database file
        print("checking database..")
        if self.model.checker():
            print("Success!")

        # Load Existing database
        data = self.model.load()
        print("Success!")

        self.fetch_working_data()


    # Initialize Main view
    def main(self):
        self.view.main()

if __name__ == "__main__":
    Tallyboard = Controller()
    Tallyboard.Initialize()

    Tallyboard.main()




# ===================  Testing  =================== #

