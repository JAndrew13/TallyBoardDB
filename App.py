import GUI
import Manager

print("Starting Application..")

app = GUI.TallyBoardDB()
workshop = Manager.Workshop()
db = Manager.Db()
gui = Manager.Gui()

count = workshop.Count()
if count == 0:
    print("EMPTY")

app.mainloop()