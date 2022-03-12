import json
import configparser

# Communicates with Controller and DataBase as intermediary
# Basic calls: Load, Save, Checker(init)



class Model:
    DATABASE_FILENAME = "Database.json"
    CONFIG_FILENAME = "config.ini"
    WORKING_DB = {}

    # current saved selections for the "submit" funtion
    current_total = 0
    current_operand = ""

    # current list of Frozen Workers
    frozen_workers = []

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

    def __init__(self):
        pass

    # Takes button inputs as codes,  deciphers, and then returns directions to controller
    def decoder(self, code):
        response = Model.CODE_LIB[code]
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
                self.create_db()
                return True

    @classmethod # Loads existing database file and convert (JSON) to (dict) -> Return data
    def load(self):
        with open(self.DATABASE_FILENAME, "r") as readfile:
            json_object = json.load(readfile)
            self.WORKING_DB = json_object
            return (json_object)

    @classmethod # Takes (dict) data, converts to (JSON) -> Saves file as "Database.JSON"
    def save(self, data):
            json_object = json.dumps(data)
            with open(self.DATABASE_FILENAME, "w") as outfile:
                outfile.write(json_object)

    @classmethod # Creates new (empty) database file as 'Database.JSON'
    def create_db(self):
        data = {}
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

# Config Class handless and operates the Config.ini file, app preferences, and settings
class Config:
    CONFIG_FILE_LOC = "config.ini"

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE_LOC)

        self.bg_color = ""
        self.frozen = []

    # Loads existing Config Data to self
    def load(self):
        # Load App Settings from .ini and save to Config object
        self.bg_color = self.config['settings']['BG_COLOR']

        # Load saved data from .ini and save to Config Object
        frozen_data = self.config['data']['frozen']
        if len(frozen_data) == 0:
            pass
        else:
            self.frozen = [name for name in frozen_data.split(', ')]

    # checks that all workers in config are still relevant
    def check_current(self, current):
        saved = self.frozen
        for name in saved:
            if name not in current:
                self.del_frozen(name)

    # Saves current app settings and data to the config file
    def save(self):
        update = ""
        for name in self.frozen:
            update += f"{name}, "
        update = update[:-2]

        self.config.set('data', 'frozen', update)
        self.config.set('settings', 'bg_color', self.bg_color)

        with open(self.CONFIG_FILE_LOC, 'w') as configfile:
            self.config.write(configfile)

    # returns saved BG color
    def get_bg(self):
        return self.bg_color

    # returns list of frozen workers
    def get_frozen(self):
        return self.frozen

    # Takes input of worker name and saves to config
    def add_frozen(self, name):
        if name in self.frozen:
            self.del_frozen(name)
        else:
            self.frozen.append(name)
            self.set_frozen()

    # takes input of worker name and removes from config
    def del_frozen(self, name):
        if name in self.frozen:
            index = self.frozen.index(name)
            self.frozen.pop(index)
            self.set_frozen()
        else:
            pass

    # Takes input of "color" and saves to .ini
    def set_bg(self, color):

        self.config['settings']['BG_COLOR'] = color
        self.config.set('settings', 'bg_color', color)
        with open(self.CONFIG_FILE_LOC, 'w') as configfile:
            self.config.write(configfile)
        self.bg_color = color

    # takes input list of [frozen_workers] and adds new items to .ini
    def set_frozen(self):
        update = ""
        for name in self.frozen:
            update += f"{name}, "
        update = update[:-2]

        self.config.set('data', 'frozen', update)
        with open(self.CONFIG_FILE_LOC, 'w') as configfile:
            self.config.write(configfile)
