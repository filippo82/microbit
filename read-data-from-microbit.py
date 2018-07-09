#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:35:52 2018

@author: filippo
"""

import serial

# serial port on raspberry pi will probably be /dev/ttyACM0
PORT = "/dev/tty.usbmodem1422"

BAUD = 115200

s = serial.Serial(PORT)
s.baudrate = BAUD
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE

while True:
        data = s.readline().decode('UTF-8')
        data_s = data.rstrip().split(' ')
        try:
            x, y, z, a, b = data_s
            print(x,y,z,a,b)

        except:
            pass

s.close()
