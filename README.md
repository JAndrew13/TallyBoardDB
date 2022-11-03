# TallyBoard DB ![stable]

<!-- ABOUT SECTION -->

TallyBoard DB is a simple CRUD application designed for a local jewelry shop to help the Project Manager track and distribute repair jobs evenly across all workers.
This task was previously time consuming, done by hand, and was vulnerable to miscalculations.
Tally Board DB exists as a simple digital counter that makes task distribution more efficient and effective.

Designed in a single Python Tkinter window in a MVC structure, TallyBoard is meant to be quick and easy to use.
Each input is autosaved as JSON data in the database, and employee workload values are automatically sorted by quantity.
This helps to effectively distribute new jobs evenly across workers as they come in.


<!-- TABLE OF CONTENTS -->
  #### Table of contents
+ [Prerequisites](#prerequisites)
+ [Installation](#installation)
+ [Usage](#usage)
+ [Directory](#directory)
+ [Contact](#contact)
+ [Acknowledgments](#acknowledgments)


<!-- Prerequisites -->

### Prerequisites

* Python ^3.1 or latest to run the app
* Python IDE to inspect files if desired (I prefer PyCharm)

<!-- Installation -->
### Installation

1. Clone or download the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```

### To run the application
Inside this project, I have included the fully packaged Windows version of the application. There is no need to install Tallyboard, it runs right from the project folder.

1. In your file explorer, navigate to "~/TallyBoardDB/Packaged" in the project folder.
2. Run "Tallyboard.exe"

### To inspect the code without running the application
1. Open the project inside your Python compatible IDE.
2. Configure your python interpreter.
  - if you're new to python, this can be a bit tricky. Please refer to the links below if you need help with this step using Pycharm.
  - [Configure Python Interpreter (JetBrains.com)](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)
  - [Configure Python Interpreter (Youtube)](https://www.youtube.com/watch?v=KLl1tXoaNgk)
3. Run "App.py" inside the root directory

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Using the App

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

### The color Picker

Located at the bottom right corner of the app window is the "Color Picker" button. This allows the user to personalize the text and window color of the application. :)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- DIRECTORY -->
## File Directory

### [/images](https://github.com/JAndrew13/)
Contains all image files used in the application

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jake Brunner -  jbbrunner10@gmail.com

LinkedIn - https://www.linkedin.com/in/jake-brunner-21760522b/

This Repository - https://github.com/jandrew13/Web-Dev-Bootcamp

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [The 2022 Web Development Course](https://www.udemy.com/course/the-complete-web-development-bootcamp)
* [The London App Brewery](https://www.londonappbrewery.com/)

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

<!-- TOOLS -->

[git-scl.com]:https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-url]:https://git-scm.com/
[Postman.com]:https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white
[Postman-url]:https://Postman.com
[Babel.com]:https://img.shields.io/badge/Babel-F9DC3e?style=for-the-badge&logo=babel&logoColor=black
[Babel-url]:Babel.com
[JavaScript.com]:https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]:https://javascript.com
[Heroku.com]: https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white
[Heroku-url]: https://heroku.com
[NodeJS.org]:https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white
[NodeJS-url]: https://nodejs.org
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com
[MongoDB.com]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://mongodb.com
[Expressjs.com]: https://img.shields.io/badge/express.js-%23404d59.svg?style=for-the-badge&logo=express&logoColor=%2361DAFB
[Expressjs-url]: https://expressjs.com
[npmjs.com]:https://img.shields.io/badge/NPM-%23000000.svg?style=for-the-badge&logo=npm&logoColor=white
[npmjs-url]:npmjs.com
[CSS3]: https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white
[HTML5]: https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white


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
