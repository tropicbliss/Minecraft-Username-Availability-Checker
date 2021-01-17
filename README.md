# Minecraft Name Checker Utility
This tiny utility is able to check multiple Minecraft usernames to determine whether they were made available recently recently.
 
 ## Installation
 1. Install the latest version of Python.
 2. Download the file [here](https://github.com/etoh53/Minecraft-Name-Checker-Utility/archive/main.zip) and extract the files.
 3. Navigate into the correct folder (MCsniperPY has a good tutorial [here](https://github.com/MCsniperPY/MCsniperPY#installing-dependencies) and enter this into your command line:
```
py -m pip install -r requirements.txt
```
Note: Linux machines might not work with the above command, so instead run this (if it still doesn't work replace `pip` with `pip3`):
```
pip install -r requirements.txt
```
4. You need to create a text file on the same directory with all the usernames that you want to check in this manner:
```
Username1
Username2
Username3
```
5. Enter this into your command line, where `<text_file>` will be the name of the file created in step 4:
```
python name_checker.py <text_file>
```
Note: For Linux machines, replace `python` with `python3`.
6. Profit!
