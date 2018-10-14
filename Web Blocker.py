import time
from datetime import datetime as dt
host_path = "C:\Python36-32\Projects\Hosts\hosts"
redirect = "127.0.0.1"

weblist_list = ["www.facebook.com","facebook.com"]


while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,12) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in weblist_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+ " " + website + "\n")
        
    else:
        with open(host_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist_list):
                    file.write(line)
            file.truncate()
        print("Few Hours")
    time.sleep(5)

    
