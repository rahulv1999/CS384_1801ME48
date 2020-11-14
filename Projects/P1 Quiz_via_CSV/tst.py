import threading
import time
import os
import sys
from pynput import keyboard
t_start = 1
def time_dis(t,roll_no,name):
    while t+1 and t_start:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        os.system(f"title {roll_no}          {name.upper()}         {timer}")
        time.sleep(1)
        t -= 1

