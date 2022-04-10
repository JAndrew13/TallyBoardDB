Tally Board DB

*** Please Note ***
Tallyboard DB is currently in version 1.0, so there is plenty of room for improvement!

*To launch and use*
- Option 1: Clone the Repo, launch TallyBoardDB.exe
- Option 2: Grab the TallyBoardDB.rar file and extract to desired location, then run TallyBoardDB.exe

*Please Note*
Version 1.0 currently supports a maximum of 9 Workers with unique names.

Project Overview
	  TallyBoard DB is a simple CRUD application designed for a local jewelry shop to help the Project Manager track and distribute repair jobs evenly across all workers. 
  This task was previously time consuming, done by hand, and was vulnerable to miscalculations. 
  Tally Board DB exists as a simple digital counter that makes task distribution more efficient and effective. 
  
	  Designed as a single Tkinter window, TallyBoard is meant to be quick and easy to use. 
  - Each input is autosaved as JSON data in the local database file.
  - Employee workloads are auto sorted by quantity, this helps to effectively distribute new jobs evenly across workers as they come in.  
  - Each worker is given a "freeze" function that pulls them from the auto sorting feature, while still maintaining their workload values.

Covered Concepts:
 - MVC Framework
 - Simple C.R.U.D. Application
 - Tkinter GUI 
 - Python
 - GitHub
 - Factory Pattern
 - Client Requested product


Future Updates:
 - Support greater worker maximum number (<9)
 - Modify data storage to allow for duplicate worker nameing
 - Add ease of use features (Quick selection memory)
 - Add Enter button detetction
