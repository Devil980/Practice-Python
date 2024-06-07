import subprocess
import time

my_list = ["Anish","harry","krish"]

for name in my_list:
    subprocess.run(["say",f"Shoutout to {name}"])
    time.sleep(1)
