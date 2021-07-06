import requests
from random import choice
import time
import os
from colorama import Fore

count = 0
hits = 0

if not os.path.exists("Results"):
    os.makedirs("Results")
if not os.path.exists("./emails.txt"):
    e= open("emails.txt", "w+")

emails = open('emails.txt', 'r')
lines = emails.readlines()
for email in lines:
    count = count + 1
    link = "https://api.gettr.com/s/email/exists?email=" + email
    data = ""
    header = {
    "accept": "application/json, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }
    response = requests.get(link, data=data, headers=header).text
    data = response
    if "OK" in data:
        if "false" in data:      
            print("{}{}".format(Fore.RED, email))
        elif "true" in data:
            open('Results/available.txt','a+').write("{}\n".format(email))
            print("{}{}".format(Fore.GREEN, email))
            hits = hits + 1
        else:
            print("{}[ERROR] {}".format(Fore.RED, email))
    else:
        print("{}[ERROR] You are rate limited!".format(Fore.RED))
    os.system(f'title GETTR Reg Checker by clout - Checked: {count}/{len(lines)} - Hits: {hits}')   
    time.sleep(0.5)
print(f"\n\n{Fore.WHITE}Done Checking")
time.sleep(20)
sys.exit()
