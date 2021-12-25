import time
try:
  from pynput.keyboard import *
except:
  import os
  os.system("pip3 install pynput")
  from pynput.keyboard import *

key = Controller()

def spam(word, times):
  for i in range(0, times):
    key.type(word)
    key.press(Key.enter)
    time.sleep(0.45)

time.sleep(3)
spam("hi", 1)
