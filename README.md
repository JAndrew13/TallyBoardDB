Tally Board DB

*** Please Note ***
Tallyboard DB is currently under major development!
  - To use the app in its current state, make sure all files are in the same folder, and you are running the current version of python. 
  - To Start the application, run the file named "Controller.py" 

Project Overview
	  TallyBoard DB is a simple CRUD application designed for a local jewelry shop to help the Project Manager track and distribute repair jobs evenly across all workers. 
  This task was previously time consuming, done by hand, and was vulnerable to miscalculations. 
  Tally Board DB exists as a simple digital counter that makes task distribution more efficient and effective. 
  
	  Designed as a single Tkinter window, TallyBoard is meant to be quick and easy to use. 
  Each input is autosaved as JSON data in the database, and employee workloads are sorted by quantity. 
  This helps to effectively distribute new jobs evenly across workers as they come in.  
  
Covered topics:
MVC Framework
C.R.U.D. Application
Tkinter 
Python
GitHub
Factory Pattern
Client Requested product

Startup and Runtime Procedures


# App Planning and Overview

# Application Startup
App → Controller (initialize Controller class object)
Controller → Model (DB Pull Request of ALL Data)
Model → Database (DB Verify (via model) Then returns ALL saved data)
Model → Controller (Unpacks and sends data to Controller)
Controller → View (Initializes View and packs data)

# Runtime
View (Mainloop() - Waits for input)
View → Controller (Receives input and sends request to Controller)
Controller → Model (takes new data and requests push from Model)
Model → DataBase packs and stores NEW data in Database
Model → Controller (Confirms successful data storage)
Controller (Receives success message)
Controller → Model (Requests DB Pull From Model)
Model → Database (Pulls Data from Database and returns to controller)
Controller → View (Controller packs data and updates View)






Print(“Starting Application”)
Create Controller(init)
Model (Communicates with controller and DB)
	Functions:

Checker(init): #Check for existing DB
If “YES” then return YES
If “NO” then CreateDB():
Return Success

Load() # pull existing JSON data 
Load JSON
Unpack JSON
Return Data

Update(Data): #Updates DB with new Entry and Saves entry to DB
Receive data
Load()
Append new data to Data
Pack data in JSON
Save()

Save(JSON): # Saves JSON Data to DB
Receive JSON Data
Overwrites DataBase With new JSON
Close DB

CreateDB():
Create DB.JSON file
Return Success or Failure

Class Worker()
	Init
	Self. name = name
	Self. tally = tally
	

View
(GUI Display - renders all elements, buttons, and widgets. Communicates to Controller)
Initialize View window
Load view objects
Take input form user

Functions:
Project() # takes data and allocation points from Controller and distributes amongst view
[inputs] Data, Allocations


Controller
(Communicates and initializes with View and Model)
	INIT(): 
self.model = Model()
		self.data = data(Dictionary)

Functions:
init_check() → Model
Request Checker() from Model
Receive Database

DB_Load() → Model
Send Request to Model.Load() to get ALL Data
Save data to self.data
Allocate Data to sections
Send allocations to View

DB_Update(data) → Model
Get data point from View 
Send Request to Model to update data

Database:(Stores the data of all employees and relative workloads)
	Format: JSON

