import sys
import time
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")
import pyo
from pyo import *

s = Server().boot()
#########
# Test 2: simple sinus 440 Hz, modulated at 6 Hz
#########
#mod = Sine(freq=6, mul=50)
#a = Sine(freq=mod + 440, mul=0.1).out()
a = Sine(freq=440, mul=0.1).out()
s.start()
time.sleep(1)
s.stop()
#s.gui(locals()) #on start gui

'''
#########
# Test 1: simple sinus 440 Hz, puis 1000 Hz
#########
a = Sine(440, 0, 0.1).out()
s.start()
time.sleep(1)
a.setFreq(1000)
time.sleep(1)
s.stop()
'''
