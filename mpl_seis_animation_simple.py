#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 21:26:04 2018

@author: filippo
"""

"""
=====
microseisms
=====

This example showcases a real-time animation of a microbit accerleromter.
"""
import serial, time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Choose the port cooresponding to the name where
# You plugged in the USB connection to the microbit
port = "/dev/tty.usbmodem1422"  

# The standard baud rate of the microbit
baud = 115200  
s = serial.Serial(port)  
s.baudrate = baud

cnt = 0
t = 0
while cnt < 10000:
    cnt += 1
    t += 0.1
    try:
        x = float(s.readline()[0:5])
        y = float(s.readline()[0:5])
        z = float(s.readline()[0:5])
        print('time is {}'.format(t))
        print(x, y, z)
    except:
        pass
#    yield t, x, y, z
    