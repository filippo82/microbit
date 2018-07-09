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


def data_stream(t=0):
    x, y, z = [], [], []
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        try:
            x = float(s.readline()[0:5])
            y = float(s.readline()[0:5])
            z = float(s.readline()[0:5])
            print(x, y, z)
        except:
            print('Sto cazzo')
            pass
        yield t, x, y, z
        

def init():
    ax.set_ylim(500, 1600)
    ax.set_xlim(0, 50)
#    del tdata[:]
#    del xdata[:]
#    del ydata[:]
#    del zdata[:]
    linex.set_data([], [])
    liney.set_data([], [])
    linez.set_data([], [])
    return linex, liney, linez

fig, ax = plt.subplots(1, 1)
linex, = ax.plot([], [], lw=1, mec='k', ms=20)
liney, = ax.plot([], [], lw=1, mec='k', ms=20)
linez, = ax.plot([], [], lw=1, mec='k', ms=20)
ax.grid(alpha=0.5)
ax.set_xlabel('time (s)')
xdata, ydata, zdata = [], [], []
tdata = []


def run(data):
    # update the data
    t, x, y, z = data
#    print(x, y, z)
    tdata.append(t)
    xdata.append(x)
    ydata.append(y)
    zdata.append(z)
    tmin, tmax = ax.get_xlim()

    if t >= tmax:
        ax.set_xlim(t, t+tmax)
        ax.figure.canvas.draw()
    linex.set_data(tdata, xdata)
    liney.set_data(tdata, ydata)
    linez.set_data(tdata, zdata)
    return linex, liney, linez

ani = animation.FuncAnimation(fig, run, data_stream, blit=False, interval=10,
                              repeat=True, init_func=init)
plt.show()

# Close serial connection
#s.close()