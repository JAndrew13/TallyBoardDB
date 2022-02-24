import json

# Communicates with Controller and DataBase as intermediary
# Basic calls: Load, Save, Checker(init)

class Model:
    DATABASE_FILENAME = "Database.json"
    WORKING_DB = {}

    current_total = 0
    current_operand = ""

    # operand-Button display labels
    OPERANDS = {1: "+", 2: "-"}

    # Button-Press action codes
    CODE_LIB = {"ADD": 1,
                "SUB": 2,
                "AddWorker": 3,
                "DeleteWorker": 4,
                "INT": 5,
                "SubmitTotal": 6,
                "ResetTotal": 7}

    MOOD_SCALE = [100,500, 1000, 2500, 3500, 5000]
    MOOD_ICONS = {0:'😁',1:'😃',2:'😅',3:'😓',4:'😣',5:'😠'}
    MOOD_COLOR = {1: 'green', 2: 'lightgreen', 3: 'yellow', 4: 'DarkYellow', 5: 'red', 6: 'DarkRed'}


    def __init__(self):
        pass

    def decoder(self, code):
        print(f"Decoding {code}")
        response = Model.CODE_LIB[code]
        print(response)
        return response

    # Reset "Current Total" variables
    def reset_total(self):
        Model.current_total = 0
        Model.current_operand = ""

# ===========  Database Handling ============= #

    @classmethod # Check for existing "Database" file (JSON)
    def checker(self):
        try:
            with open(self.DATABASE_FILENAME, 'r'):
                return True

        except FileNotFoundError:
            with open(self.DATABASE_FILENAME, "w"):
                print("Database file created")
                self.create_db()
                return True

    @classmethod # Loads existing database file and convert (JSON) to (dict) -> Return data
    def load(self):
        with open(self.DATABASE_FILENAME, "r") as readfile:
            json_object = json.load(readfile)
            print("loading database..")
            self.WORKING_DB = json_object
            return (json_object)

    @classmethod # Takes (dict) data, converts to (JSON) -> Saves file as "Database.JSON"
    def save(self, data):
            json_object = json.dumps(data)
            with open(self.DATABASE_FILENAME, "w") as outfile:
                outfile.write(json_object)
            print("Database template saved")

    @classmethod # Creates new (empty) database file as 'Database.JSON'
    def create_db(self):
        data = {}
        print("Creating Database Template")
        self.save(data)

# =============  Worker Construction / Management operators  ============== #

# Workshop class modifys the Controllers "Working Data"
# takes controller and data as INIT variables
class Workshop:
    def __init__(self, controller, data):
        self.controller = controller
        self.data = data

    # Takes "Worker name" as input, adds to self.data -> returns "data"
    def add_worker(self, f_name):
        self.data[f_name] = 0
        return self.data

    # Takes "Worker name" as input, removes name from self.data -> returns "data"
    def del_worker(self, name):
        f_name = name
        if f_name in self.data:
            self.data.pop(f_name)
        return self.data

    # Takes "Worker name" and "Amount" as input, adds to self.data -> returns "data"
    def add_tally(self, name, amount):
        self.data[name] += amount
        return self.data

    # Takes "Worker name" and "Amount" as input, subs from self.data -> returns "data"
    def sub_tally(self, name, amount):
        self.data[name] -= amount
        return self.data

    # Takes "Worker name" as input -> returns "Tally" of "Worker Name"
    def get_Tally(self, name):
        return (self.data[name])

    # Takes input of "Worker Name" -> returns 'Worker Temperature"
    def get_temp(self, name):
        pass
