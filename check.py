try:
    import sys
    import os
    import time
    import requests
    import re
    import math
    import concurrent.futures
except ImportError:
    print("Trying to install the required modules! THIS MAY DISPLAY LARGE ERRORS!\nPlease try to run this script again once all of the modules have been successfully installed.\n\n")
    input("press enter to start installing... ")
    os.system("py -m pip install -r requirements.txt")
    os.system("python -m pip install -r requirements.txt")
    os.system("python3 -m pip install -r requirements.txt")
    input("\n\ndone installing modules! please restart the script now. Press enter to continue... ")
    sys.exit()

def check_username(username):
    retry = True
    while retry:
        retry = False
        result = bool(regex.search(username))
        if not (result or (len(username) < 3) or (len(username) > 16)):
            res = requests.get('https://api.mojang.com/users/profiles/minecraft/' + username)
            if res.status_code == 200:
                print(f'{username} was taken.')
            elif res.status_code == 204:
                print(f'{username} is available or never used.')
                # multithreading with GIL so don't need to worry about race conditions, whew!
                available_names.append(username)
            elif res.status_code == 429:
                end_time = time.time()
                global start_time
                time_to_wait = math.ceil(600 - (end_time - start_time))
                global rate_limited
                if not rate_limited:
                    rate_limited = True
                    print(f'Request is being refused due to IP being rate limited. Waiting {time_to_wait} seconds before reattempting...')
                retry = True
                time.sleep(time_to_wait)
                rate_limited = False
                start_time = time.time()
            else:
                res.raise_for_status()
                print(f'Unhandled HTTP status code: {res.status_code}. Exiting...')
                sys.exit()
        else:
            print(f'{username} is an invalid username.')
            invalid_names.append(username)

filepath = sys.argv[1]
if not os.path.isfile(filepath):
    print(f'File path {filepath} does not exist. Exiting...')
    sys.exit()
available_names = []
invalid_names = []
with open(filepath) as name_list:
    username_list = [line.rstrip('\n') for line in name_list]
    if not username_list:
        print(f'{filepath} is empty. Exiting...')
        sys.exit()
regex = re.compile(r'[^a-zA-Z0-9_.]')
rate_limited = False
start_time = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    try:
        executor.map(check_username, username_list)
    except Exception as exc:
        print(f'There is a problem: {exc}. Exiting...')
        sys.exit()
print()
print(f'Available username(s): {available_names}')
if invalid_names:
    print(f'Invalid username(s): {invalid_names}')
