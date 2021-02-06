import sys
import os
import time
from datetime import datetime
import requests
import bs4

def main():
    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()
    available_names = []
    invalid_names = []
    with open(filepath) as name_list:
        username = name_list.readline().strip()
        while username:
            try:
                retry = False
                now = datetime.utcnow()
                res = requests.get('https://namemc.com/search?q=' + username)
                try:
                    res.raise_for_status()
                except Exception as exc:
                    print("There was a problem: {}".format(exc))
                    if "429" in str(exc):
                        print("Request is being refused due to IP being rate limited. Waiting 10 minutes before reattempting...")
                        retry = True
                        time.sleep(600)
                    continue
                namemc_soup = bs4.BeautifulSoup(res.text, 'html.parser')
                available_time = namemc_soup.find("time", {"id": "availability-time"}).attrs["datetime"]
                available_time = datetime.strptime(available_time, '%Y-%m-%dT%H:%M:%S.000Z')
                wait_time = available_time - now
                print("{} is available at {} ({} later).".format(username, available_time, wait_time))
                available_names.append(username)
            except AttributeError:
                print("{} was taken or unavailable.".format(username))
            finally:
                if retry == False:
                    if username.isalnum() == False:
                        print("{} is an invalid username.".format(username))
                        invalid_names.append(username)
                    username = name_list.readline().strip()
        print()
        print("Available username(s): {}".format(available_names))
        if invalid_names:
            print("Invalid username(s): {}".format(invalid_names))

if __name__ == '__main__':
    main()
