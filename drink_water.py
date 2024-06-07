import subprocess
import time 

def send_notification(title, subtitle, message):
    script = f'display notification "{message}" with title "{title}" subtitle "{subtitle}"'
    subprocess.run(['osascript', '-e', script])

def notifications_periodically(title,subtiitle,message,time_interval):
    while True:
        send_notification(title,subtiitle,message)
        time.sleep(time_interval)


notifications_periodically("drink Water", "water time", "You have been dehydrated dink water",1600)

