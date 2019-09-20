#coding utf-8
import time
import datetime
import random
import os

morning_list = [
    "https://www.youtube.com/watch?v=MEmvk3ZSs0M&t=941s",
    "https://www.youtube.com/watch?v=GkqhHEAy1zw&t=232s",
    "https://www.youtube.com/watch?v=pFfvUMqiy34",
    "https://www.youtube.com/watch?v=d0R0gFvmaMk&t=8s",
    "https://www.youtube.com/watch?v=OWfBDTR6z6M"
    ]
noon_list = [
    "https://www.youtube.com/watch?v=74iHoCM83Mg&t=5s",
    "https://www.youtube.com/watch?v=EWbgwDfiVf8",
    "https://www.youtube.com/watch?v=8SJ1mm5c7N0",
    "https://www.youtube.com/watch?v=giouzUH5rOc"
    ]

eveinig_list=[
    "https://www.youtube.com/watch?v=RDjimODZtQM&t=5s",
    "https://www.youtube.com/watch?v=LbzTAa7YJqE",
    "https://www.youtube.com/watch?v=ZcThrAU9yLk",
    "https://www.youtube.com/watch?v=PErqizZqLjI&t=17s",
    "https://www.youtube.com/watch?v=cyyZYUrVcqA"
    ]

def music_change(current_hour):

    os.system('killall chromium-browser')

    if(current_hour >= 7 and current_hour < 12):
        music = random.choice(morning_list)
    elif(current_hour >=  12 and current_hour < 19):
        music = random.choice(noon_list)
    elif(current_hour >=  19 and current_hour < 24):
        music = random.choice(eveinig_list)
    else:
        return 0

    string = 'chromium-browser ' + music
    os.system(string)

def main():
    current_hour= datetime.datetime.now().hour
    previous_hour = current_hour
    music_change(current_hour)

    while(True):
        current_hour = datetime.datetime.now().hour
        print("current_hour:",current_hour,"previous_hour:",previous_hour)
        if(previous_hour != current_hour):
            music_change(current_hour)
        previous_hour = current_hour
        time.sleep(30)

if __name__=="__main__":
    main()
