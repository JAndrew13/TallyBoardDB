import json

# Communicates with Controller and DataBase as intermediary
# Basic calls: Load, Save, Checker(init)

class Model:
    DATABASE_FILENAME = "Database.json"
    CODE_LIB = {"ADD": 1,
                "SUB": 2,
                "AddWorker": 3,
                "DeleteWorker": 4,
                "INT": 5,
                "SubmitTotal": 6,
                "ResetTotal": 7}
    OPERANDS = {
        1: "(+)",
        2: "(-)"
    }

    WORKING_DB = {}

    current_total = 0
    current_operand = ""

    def __init__(self):
        pass

    def decoder(self, code):
        print(f"Decoding {code}")
        print(f"current total: {Model.current_total}")
        #check for integer

        int_test = [item for item in code.split("-")]
        if int_test[0] == "INT":
            int_val = int_test[1]
            print(f"integer value = {int_val}")
            response = 5
            Model.current_total += int(int_val)

        else:
            response = Model.CODE_LIB[code]
        return response

    def reset_total(self):
        Model.current_total = 0
        Model.current_operand = ""

    def create_worker(self, name):
        workshop.Add_worker(f_name=f"{name}")



# ===========  Database Handling ============= #
    @classmethod
    def checker(self):
        try:
            with open(self.DATABASE_FILENAME, 'r'):
                return True

        except FileNotFoundError:
            with open(self.DATABASE_FILENAME, "w"):
                print("Database file created")
                self.create_db()
                return True

    @classmethod
    def load(self):
        with open(self.DATABASE_FILENAME, "r") as readfile:
            json_object = json.load(readfile)
            print("loading database..")
            self.WORKING_DB = json_object
            return (json_object)

    @classmethod
    def save(self, data):
            json_object = json.dumps(data)
            with open(self.DATABASE_FILENAME, "w") as outfile:
                outfile.write(json_object)
            print("Database template saved")

    @classmethod
    def create_db(self):
        data = {}
        print("Creating Database Template")
        self.save(data)

# =============  Worker Construction  ============== #

class Workshop:
    def __init__(self):
        self.emp_names = {}

    def Roster(self):
        for name in self.emp_names:
            print(name)

    def Count(self):
        print(self.emp_count)

    def Add_worker(self, f_name):
        self.emp_names[f_name] = 0

    def Sub_worker(self, name):
        f_name = name
        if f_name in self.emp_names:
            self.emp_names.pop(f_name)

    def Add_tally(self, name, amount):
        self.emp_names[name] += amount

    def Sub_tally(self, name, amount):
        self.emp_names[name] -= amount

    def Get_Tally(self, name):
        return (self.emp_names[name])

    def Get_Stats(self, name):
        if name in self.emp_names:
            tally = self.emp_names[name]
            return f"{name}, ${tally}"


#
# # empCount = 3
# # i=0
#
# while i<3:
#     workshop.add_worker()
#     i+=1
# print(workshop.emp_names)
# print(workshop.emp_names["jake"])
workshop = Workshop()