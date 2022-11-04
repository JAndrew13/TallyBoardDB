
# TallyBoard DB ![stable]
<a name="readme-top"></a>
<!-- ABOUT SECTION -->


TallyBoard DB is a simple MVC/CRUD application designed for a local jewelry shop to help the Project Manager track and distribute repair jobs evenly across all workers.
This task was previously time consuming, done by hand, and was vulnerable to miscalculations. This software exists as a simple digital counter that makes task distribution more efficient and effective.

This was my first attempt at making a full application from start to finish for a client, using pure python. Designed in a single Python Tkinter window, TallyBoard is meant to be quick and easy to use. Each input is autosaved as JSON data in the local database file, and employee workload values are automatically sorted and displayed by quantity.
This helps to effectively distribute new jobs evenly across workers as they come in.


<!-- TABLE OF CONTENTS -->
  #### Table of contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
	1.[Roster](#usage-roster)
	2.[Add/Del Workers](#usage-workers)
	3.[Value Selector](#usage-value-selector)
	4.[Action Buttons](#usage-action-buttons)
	5.[The Tally Board](#usage-tally-board)
	6.[Polor Picker](#usage-color-picker)
5. [Directory](#directory)
6. [Operations](#operations)
	1. [App.py](#app.py)
	2. [Contoller.py](#controller.py)
	3. [Model.py](#model.py)
	4. [View.py](#view.py)
	5. [Database](#database)
	6. [Config](#config)
7. [Contact](#contact)


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
# Using the App (client-side)


<a name="usage-roster"></a>
## The Roster Display

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard3.jpg)

This area of the application simply displays all of the Available workers saved in the database, while also acting as a selector for any actions preformed in the app. The default selection is the top-most worker, but this selection can be changed by clicking a different worker's name.
A worker must be selected to:
- Add or remove values to the workers total
- Delete a worker from the Roster

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="usage-workers"></a>
## Add/Remove Available workers


![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard2.jpg)

The two buttons at the top of the app window are used for adding and removing workers from the local database.
   Adding a worker to the database:
   * Enter the new workers name in the text box located in the top right.
   * Click the "Add worker" button.

   Removing a worker from the database:
   * Highlight the desired worker's name from the roster by clicking their name.
   * Click the "Del Worker" button.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="usage-value-selector"></a>
## Value Selector

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="usage-action-buttons"></a>
## Total Value Action Buttons

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard5.jpg)

These four action buttons tell the app what to do once you have set a total value.
* "Add (+)" - Sets the app to 'addition mode' for the entry
* "Sub (+)" - Sets the app to 'subtraction mode' for the entry.
* "Submit" - Submits the update to the DataBase, updating the worker total and refreshing the tally board below.
* "Reset" - Resets the current total value back to zero.

*Each time you press "Submit", you must have either the "Add (+)" or "Sub (-)" button selected. This tells the app how to update the selected workers total.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="usage-tally-board"></a>
## The Tally board

![TallyBoardDB overview image](https://github.com/JAndrew13/TallyBoardDB/blob/master/Images/Tallyboard6.jpg)

This is the main area of interest for the app. The Tally Board pulls all of the workers from the Roster and keeps track of their total workloads. Each time a change is made in app, the Tally Board will automatically refresh and sort the workers by their totals in ascending order. When new work comes into the shop, the worker at the top of the list would be the next to receive a job because they have the smallest workload.

Next to each worker are two buttons, "Reset" and "Freeze".
  * The "Reset" button will reset the workers total back to zero, moving them to the bottom of the list.
  * The "Freeze" button is meant to be used when the worker is out of the office, on vacation, sick, etc. When a worker is 'frozen', they are removed from the sorting function and placed at the bottom of the tally board until 'unfreeze' is selected. This helps the user remember not to apply new jobs to that worker until they return to the office.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="usage-color-picker"></a>
## The Color Picker

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

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- OPERATIONS -->
# Operations
Here, I'd like to provide an brief explanation of the code, and how the program operates as a whole. The focus of this project was to really drill down on the "MVC" design pattern. Listed below are the six main files that make up the program, along with a short description of their functions and purpose.

<a name="app.py"></a>
 ## `App.py`
 
 This is the starting point for the application. This file simply imports and runs the controller file. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="controller.py"></a>
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
 
 <p align="right">(<a href="#readme-top">back to top</a>)</p>
 <a name="model.py"></a>
 ## `Model.py`
 
 The Model class is the "gate keeper" to the apps long term stored data. It is the only entity in the application that is permitted to access the database - allowing it to read, write, and update the data as needed. While not entirely necessary for this specific program, It is essential in standard "MVC" architecture, so I decided to include it. 

The Model file itself contains three classes - The Model, Workshop, and Config class, each containing a set of class functions. I did this to make sure that the database related functions weren't "out in the open", but instead contained inside the *permitted* Model class.

**The Model Class**
Responsible for all database connection related functionality.

`Decoder`
The decoder is a specific function used in conjunction with the controller to help determine the source, value, and intention of a button press. This function could also be held inside the controller, but I decided to keep in the Model, because it handles "raw data". A bit on how this works, is all buttons in the view output 'action codes', which are stored in the model's "*CODE_LIB*" property. These codes get interpreted by the model and sent back to the controller for action. Its a bit odd I suppose, but it worked for me. 

`Database handeling`
 These four functions are responsible for checking for past data, creating a new database, parsing and converting JSON data, and doing basic 'save' and 'load' processes. 

**The Workshop Class**
 This class exists to handle 'workshop' related data, things like worker names, the current roster, whos out of the office, and how much work a specific worker has. Its functions can add and remove workers from the app, modify their totals, and fetch specific pieces of their information. 

**The Config Class**
The Config class operates the Config.ini file, app preferences, settings, and any related changes made by the user. 

`Load/Save/Check Config file` 
~ These functions check and load startup settings when the app opens, as well as save new preferences to the config.

`get/set/return bg`
~   Handles settings related to the apps colored background.

`get/add/del/set frozen`
~ Responsible for fetching and storing save data relating to workers who have been 'frozen' during the last app use.
 
 <p align="right">(<a href="#readme-top">back to top</a>)</p>
 <a name="view.py"></a>
 ## `View.py`
 
 Once the controller is loaded, it calls to the view file, and sends over the settings defined in the config file. Here, the view class uses Python's Tkinter to draw up the app UI using it's functions and class properties. Once the app window has been rendered, the view class uses event listeners to detect and changes made by the User, and returns all event data back to the controller. View functions are grouped in the following categories:
 
 `Widgets and view creation`
 ~ Uses factory patterns to populate all buttons, displays, text boxes, and related triggers
 
 `Text entry validators  `
 ~ Receives all text entries and validates that appropriate characters are being applied. This prevents alpha characters from being sent into the controllers value calculation functions.
 
 `Custom number entry functions`
~ Handles integer entries in the custom total box and assists controller in displaying the pre-submitted tally amount.
 
 `Data updating functions`
 ~ Responsible for rendering and updating the worker display, as well as updating the view long and short term data. "Short term" data being bits of information that are not temporary and are never stored in the database. "Long Term" data being things like worker name changes and total values.
 
 `App modifiers`
 ~ These functions deal with rendering changes to the app's UI - i.e. background color.
 
 <p align="right">(<a href="#readme-top">back to top</a>)</p>
 <a name="database.py"></a>
 ## `Database.json`
 
 The 'Database.json' file will be created in the root project folder when the app opens for the first time. This file is responsible for holding all of the *long term* information used in the app at runtime. It is only accessible via the model, and keeps all data stored in JSON format. 

Because of the *non-sensitive* nature of this application, I felt that storing data in JSON format would be just fine. There currently is no hashing or security applied the database other than 'model only' access. In a more high level application however, sensitive data should be stored in a more secure way.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<a name="config.py"></a>
## `Config.ini`

The config file contains app startup preferences relating to visual styling, while also containing a shorthand memory of any workers set to frozen when the app was last closed. Like the database file, the Config.ini will be created in the root project folder on startup if one doesnt currently exist. 



<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Jake Brunner -  jbbrunner10@gmail.com

LinkedIn - https://www.linkedin.com/in/jake-brunner-21760522b/

This Repository - https://github.com/jandrew13/TallyboardDB

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->

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

	Format: JSON
=======

Future Updates:
 - Support greater worker maximum number (<9)
 - Modify data storage to allow for duplicate worker nameing
 - Add ease of use features (Quick selection memory)
 - Add "Enter" button detetction
