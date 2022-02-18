import GUI
import Manager


print("Starting Application..")



if __name__ == "__main__":
    app = GUI.TallyBoardDB()
    workshop = Manager.Workshop()
    db = Manager.Db()
    gui = Manager.Gui()

    app.mainloop()