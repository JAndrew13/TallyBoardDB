
# TallyBoard DB ![stable]

<!-- ABOUT SECTION -->

TallyBoard DB is a simple MVC/CRUD application designed for a local jewelry shop to help the Project Manager track and distribute repair jobs evenly across all workers.
This task was previously time consuming, done by hand, and was vulnerable to miscalculations. This software exists as a simple digital counter that makes task distribution more efficient and effective.

This was my first attempt at making a full application from start to finish for a client, using pure python. Designed in a single Python Tkinter window, TallyBoard is meant to be quick and easy to use. Each input is autosaved as JSON data in the local database file, and employee workload values are automatically sorted and displayed by quantity.
This helps to effectively distribute new jobs evenly across workers as they come in.


<!-- TABLE OF CONTENTS -->
  #### Table of contents
+ [Prerequisites](#prerequisites)
+ [Installation](#installation)
+ [Usage](#usage)
+ [Directory](#directory)
+ [Contact](#contact)


<!-- Prerequisites -->

### Prerequisites

* Python ^3.1 or latest to run the app
* Python IDE to inspect files if desired (I prefer PyCharm)

<!-- Installation -->
### Installation

1. Clone or download the repo
   ```sh
   git clone https://github.com/JAndrew13/TallyBoardDB.git
   ```

### To run the application
Inside this project, I have included the fully packaged Windows version of the application. There is no need to install Tallyboard, it runs right from the project folder.

1. In your file explorer, navigate to "~/TallyBoardDB/Distribution" in the project folder.
2. Exract the "TallyBoardDB.rar" file to your desired location.
3. Run "Tallyboard.exe" (no installation required)

### To inspect the code without running the application
1. Open the project inside your Python compatible IDE.
2. Configure your python interpreter.
  - if you're new to python, this can be a bit tricky. Please refer to the links below if you need help with this step using Pycharm.
  - [Configure Python Interpreter (JetBrains.com)](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
  - [Configure Python Interpreter (Youtube)](https://www.youtube.com/watch?v=KLl1tXoaNgk)
3. Run "App.py" inside the root directory

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Using the App (client-side)

### The Roster Display

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard3.jpg)

This area of the application simply displays all of the Available workers saved in the database, while also acting as a selector for any actions preformed in the app. The default selection is the top-most worker, but this selection can be changed by clicking a different worker's name.
A worker must be selected to:
- Add or remove values to the workers total
- Delete a worker from the Roster

### Add/Remove Available workers

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard2.jpg)

The two buttons at the top of the app window are used for adding and removing workers from the local database.
   Adding a worker to the database:
   * Enter the new workers name in the text box located in the top right.
   * Click the "Add worker" button.

   Removing a worker from the database:
   * Highlight the desired worker's name from the roster by clicking their name.
   * Click the "Del Worker" button.

### Value Selector

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard4.jpg)

When adding or subtracting values from a workers total using the Value Selector, you can either use the custom input box or the quick select number buttons.
The quick select buttons will automatically add to the total each time a button is clicked. For example, if I want to add a job worth $561 to Jake's total, I would
select "Jake" from the roster display, then do the following:

  * Type "561" in the Total Value text box
  * Click the "Add (+)" button
  * Click the "Submit" button to confirm the new change.

  ~OR~

  * Select the Quick Value buttons, "500", "50", "10", "1"
  * Click the "Add (+)" button.
  * Click the "Submit" button to confirm the new change.


### Total Value Action Buttons

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard5.jpg)

These four action buttons tell the app what to do once you have set a total value.
* "Add (+)" - Sets the app to 'addition mode' for the entry
* "Sub (+)" - Sets the app to 'subtraction mode' for the entry.
* "Submit" - Submits the update to the DataBase, updating the worker total and refreshing the tally board below.
* "Reset" - Resets the current total value back to zero.

*Each time you press "Submit", you must have either the "Add (+)" or "Sub (-)" button selected. This tells the app how to update the selected workers total.

### The Tally board

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard6.jpg)

This is the main area of interest for the app. The Tally Board pulls all of the workers from the Roster and keeps track of their total workloads. Each time a change is made in app, the Tally Board will automatically refresh and sort the workers by their totals in ascending order. When new work comes into the shop, the worker at the top of the list would be the next to receive a job because they have the smallest workload.

Next to each worker are two buttons, "Reset" and "Freeze".
  * The "Reset" button will reset the workers total back to zero, moving them to the bottom of the list.
  * The "Freeze" button is meant to be used when the worker is out of the office, on vacation, sick, etc. When a worker is 'frozen', they are removed from the sorting function and placed at the bottom of the tally board until 'unfreeze' is selected. This helps the user remember not to apply new jobs to that worker until they return to the office.

### The Color Picker

Located at the bottom right corner of the app window is the "Color Picker" button. This allows the user to personalize the text and window color of the application. :)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DIRECTORY -->
## File Directory

 `/images` 
 Contains all image files used in the application and readme.

`/distribution`
Contains the packaged .RAR file of the completed project, ready to run on windows pc

`/venv`
Contains boiler-plate files related to the virtual environment setup for python IDE. 

`/root`
Contains the files related to the apps main functionality.


<!-- OPERATIONS -->
# Operations
Here, I'd like to provide an brief explanation of the code, and how the program operates as a whole. The focus of this project was to really drill down on the "MVC" design pattern. Listed below are the six main files that make up the program, along with a short description of their functions and purpose.

 ## `App.py`
 This is the starting point for the application. This file simply imports and runs the controller file. 

 ## `Controller.py`
 After being triggered by the App.py file on startup, the controller class starts by loading the model, view, config settings. Its main job is to receive requests from the View, and determine how to respond. Its functions are separated into four categories:
 
 `Event Handling` 
 ~ The event handling functions work alongside the model to receive user inputs and determine how to respond.
 
 `Data Managment`
~ Contains all database control calls for fetching, updating, and deleting data stored data. These calls then get sent to the Model for actions.

 `App initialization`
~ Initializes the programs view, checks for previously saved config data and applies it to the app.
 
 `Config Operations`
~ Pulls saved program settings from the config file if any exist.
 
 ## `Model.py`
 
 ## `View.py`
 

 
 ## `Database.json`
 
 ## `Config.ini`



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jake Brunner -  jbbrunner10@gmail.com

LinkedIn - https://www.linkedin.com/in/jake-brunner-21760522b/

This Repository - https://github.com/jandrew13/TallyboardDB

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->

[product-screenshot]: images/screenshot.png

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew

<!-- STATUS MARKERS -->

[stable]: http://badges.github.io/stability-badges/dist/stable.svg
[unstable]: http://badges.github.io/stability-badges/dist/unstable.svg
[depreciated]: http://badges.github.io/stability-badges/dist/deprecated.svg
[experimental]: http://badges.github.io/stability-badges/dist/experimental.svg
[frozen]: http://badges.github.io/stability-badges/dist/frozen.svg
[locked]: http://badges.github.io/stability-badges/dist/locked.svg

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues

<!-- USED TOOLS -->

[git-scl.com]:https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-url]:https://git-scm.com/

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
=======

Future Updates:
 - Support greater worker maximum number (<9)
 - Modify data storage to allow for duplicate worker nameing
 - Add ease of use features (Quick selection memory)
 - Add "Enter" button detetction
