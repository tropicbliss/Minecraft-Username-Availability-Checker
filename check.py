import sys
import os
import time
import requests
import re
import math

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    available_names = []
    invalid_names = []
    with open(filepath) as name_list:
        username = name_list.readline().strip()
        regex = re.compile(r'[^a-zA-Z0-9_.]')
        retry = False
        start_time = time.time()
        while username:
            result = bool(regex.search(username))
            if not (result or (len(username) < 3) or (len(username) > 16)):
                retry = False
                res = requests.get('https://api.mojang.com/users/profiles/minecraft/' + username)
                if res.status_code == 200:
                    print("{} was taken.".format(username))
                elif res.status_code == 204:
                    print("{} is available or never used.".format(username))
                    available_names.append(username)
                elif res.status_code == 429:
                    end_time = time.time()
                    time_to_wait = math.ceil(600 - (end_time - start_time))
                    print("Request is being refused due to IP being rate limited. Waiting {} seconds before reattempting...".format(time_to_wait))
                    retry = True
                    time.sleep(time_to_wait)
                    start_time = time.time()
                else:
                    try:
                        res.raise_for_status()
                    except Exception as exc:
                        print("There is a problem: {}".format(exc))
                    else:
                        print("Unhandled HTTP status code: {}. Program exiting...".format(res.status_code))
                    finally:
                        sys.exit()
            else:
                print("{} is an invalid username.".format(username))
                invalid_names.append(username)
            if not retry:
                username = name_list.readline().strip()
        print()
        print("Available username(s): {}".format(available_names))
        if invalid_names:
            print("Invalid username(s): {}".format(invalid_names))

if __name__ == '__main__':
    main()
