# Minecraft Username Availability Checker

This tiny utility is able to check Minecraft usernames in bulk to determine whether they were made available recently.

This version includes multithreading support which drastically improves speed, making this one of the fastest username checkers ever. You'll get rate limited almost immediately, guaranteed!

<img src="https://media.giphy.com/media/zw8YsfZfx0rzTsM4Vn/giphy.gif" width="550">

## Credits

[MCsniperPY](https://github.com/MCsniperPY/MCsniperPY) (for the readme and `install.sh`). ♥️

## Dependencies

- [requests](https://2.python-requests.org/en/latest/)

## Installation

### Linux easy installation

Run `bash -c "curl -sLo check.sh https://raw.githubusercontent.com/chronicallyunfunny/Minecraft-Username-Availability-Checker/v3/install.sh && chmod +x check.sh && ./check.sh"` in your terminal to install the checker.

### Windows installation

You will have to have a few things installed before running the checker. This installation guide assumes that you are on a 64bit Windows system.

First, you will need to install Python. It's recommended to use either version `3.8.5` or `3.8.6`. You must use a Python version above `3.0`. 

### Installing Python

Go to the following link and download Python:

`https://www.python.org/ftp/python/3.8.5/python-3.8.5-amd64.exe`

Once you have opened the installer, make sure that you add Python to path. Your installer should look like this:

<img align="center" src="https://i.imgur.com/iefWNyw.png">

Run through the installer as normal, then download the Minecraft Username Availability Checker files.

### Downloading Minecraft Username Availability Checker

Download the following file [here](
https://github.com/etoh53/Minecraft-Name-Checker-Utility/archive/v3.zip).

Extract the folder to somewhere easily accessible, such as your desktop.

### Installing dependencies

You now need to open a command prompt to the Minecraft Username Availability Checker path. An easy way to do this is by opening the folder and typing `cmd` in the path.

Your command prompt should have a line similar to this:

`C:\Users\%USERNAME%\%PATH%\Minecraft-Username-Availability-Checker-3>`

If there is nothing after your Windows username, you will have to type the following command:

`cd path_to_folder`

Once you have a commant prompt open to the correct path, you should type the following command:

`py -m pip install -r requirements.txt`

If you get the following message:

`'py' is not recognized as an internal or external command, operable program or batch file.`

then you will need to reinstall Python following the guide above, make sure that you added Python to PATH.

Otherwise, you have installed the correct dependencies and can follow on with the tutorial.

## Setup

You need to create a text file on the same directory where the unzipped files are with all the usernames that you want to check in this manner:

```
Username1
Username2
Username3
```

## Running the checker

To run the checker you want to open a command prompt window where Minecraft Username Availability Checker is located.

Once the window is open, you want to type the following command:

### Windows:

`py check.py <text_file>`

### Linux easy installation:

`./check.sh <text_file>`

where `<text_file>` is the name of the file you created in the [Setup](https://github.com/chronicallyunfunny/Minecraft-Username-Availability-Checker/blob/v3/README.md#setup) section above.

For example:

`py check.py example.txt`

Assuming nothing went wrong, the checker should now be running.

## FAQ

### Why does the script stop checking names after a while?

After a few requests, requests made to Mojang servers will get rate limited. Therefore the script waits for a while before resuming requests. Don't worry, this is normal. For Linux users running this off a VPS, feel free to use `screen` to run this script in the background.

### Why can't I obtain a username even if it shows up as available?

The username is most likely blocked by bots or Mojang.
