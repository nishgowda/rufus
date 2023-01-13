# Was it Rufus?
Take home assignment.

## Instructions - How to Run:
### Step 1: Install Requirements:
First, install the requirements from ```requirements.txt``` (preferably with a virtual environment) using pip with ```pip install -r requirements.txt```

### Step 2: Run the program
You can the run the python script by running the ```rufus.py``` script along with the directory path of the git repository you'd like to use this on as an argument. Here's an example:	

```
python3 rufus.py ~/fun/my_project
```

### Step 3: See Output
The output you get from the script should look like this if you passed in a valid repository:

```
active branch: master
local changes: False
recent commit: False
blame Rufus: False
```

Note that if you pass in an invalid directory (or you pass in no arguments at all) you will get an error message notifying you of that and the program will terminate.

For example, if you pass in an invalid git directory, you'll receive the following error message: ```Invalid directory```. Similarly, if you don't pass in any argument when running the script you'll get the following error message: ```Please enter a directory```.


