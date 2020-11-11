import threading 
import time
import os
import sys
from pynput import keyboard

def key_map():
    # print("u pressed ",key)
    # print(type(key))
    
    print("unattempted question")



# with keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+<alt>+h'),p()) as key:


listener = keyboard.GlobalHotKeys({'<ctrl>+<alt>+h':key_map})
listener.start()
hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    key_map)
time.sleep(10)
