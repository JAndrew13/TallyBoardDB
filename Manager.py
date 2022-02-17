import json

class Workshop:
    def __init__(self):
        self.emp_names = {}
        self.emp_count = len(self.emp_names)

    def Roster(self):
        for name in self.emp_names:
            print(name)

    def Count(self):
        print(self.emp_count)
        return self.emp_count

    def Add_worker(self):
        f_name = input("first name?").lower()
        self.emp_names[f_name] = 0

    def Sub_worker(self):
        f_name = input("first name?").lower()
        if f_name in self.emp_names:
            self.emp_names.pop(f_name)

    def Add_tally(self, name, amount):
        workshop.emp_names[name] += amount

    def Sub_tally(self, name, amount):
        workshop.emp_names[name] -= amount

class Db:
    def __init__(self):
        self.data = {}

    def db_push(self):
        json_object = json.dumps(self.data)
        with open("Database.json", "w") as outfile:
            outfile.write(json_object)

    def db_pull(self):
        with open('Database.json', 'r') as openfile:
            json_object = json.load(openfile)
        return(json_object)



class Gui:
    def __init__(self):
        pass

#
# # empCount = 3
# # i=0
#
# while i<3:
#     workshop.add_worker()
#     i+=1
# print(workshop.emp_names)
# print(workshop.emp_names["jake"])
