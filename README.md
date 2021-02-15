# Minecraft Username Availability Checker
This tiny utility is able to check Minecraft usernames in bulk to determine whether they were made available recently.

<img src="https://media.giphy.com/media/WSdNo4sktc8AgQut4x/giphy.gif" width="300">
Note: Speed depends on your ping to Mojang servers.

## New version?
This newer version uses Mojang's API instead of obtaining data through NameMC via web scraping.

### Advantages:
- Way faster
- Less stringent rate limiter
- 1 dependency to download instead of 2

### Disadvantages:
- Inability to get username availability time (possible but I am lazy).
- More likely to break if Mojang changes its API

Feel free to use the older version (in the other branch) which still works fine at the time of writing (but there's really no point).

## Dependencies
- requests
 
## Installation and Usage
1. Install the latest version of Python 3.
2. Download the file [here](https://github.com/etoh53/Minecraft-Name-Checker-Utility/archive/v2.zip) and extract the files.
3. Navigate into the correct folder (MCsniperPY has a good tutorial [here](https://github.com/MCsniperPY/MCsniperPY#installing-dependencies) and enter this into your command line:
```
py -m pip install -r requirements.txt
```
Note: The above command might not work on Linux, so run this instead (if it still doesn't work replace `pip` with `pip3`):
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
py check.py <text_file>
```
For example:
```
py check.py example.txt
```
Note: For Linux, replace `py` with `python3`.

6. Profit!

Note: After a few requests, requests made to NameMC will get rate limited. Therefore the script waits for a while before resuming requests. For Linux users running this off a VPS, feel free to use `screen` to run this script in the background.

## Why can't I obtain a username even if it shows up as available?
The username is most likely blocked by bots or Mojang.

## Multithreading support?
Multithreading support coming soon, which will make this one of the fastest Minecraft username availability checkers ever!
