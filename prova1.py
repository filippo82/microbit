#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 23:39:49 2018

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

port = "/dev/tty.usbmodem1422"  
baud = 115200  
s = serial.Serial(port)  
s.baudrate = baud
s.parity   = serial.PARITY_NONE
s.databits = serial.EIGHTBITS
s.stopbits = serial.STOPBITS_ONE


def data_gen(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)

def data_stream(t=0):
    cnt = 0
    while cnt < 1000:
        cnt += 1
        t += 0.1
        data = s.readline().decode('UTF-8')
        data_s = data.rstrip().split(' ')
        try:
            x, y, z = list(map(float, data_s[0:3]))
            a, b = data_s[3:5]
#            print(t, cnt, x, y, z, a, b)
#            print(type(x))
        except:
            pass
        
        yield t, z


def init():
    ax.set_ylim(-1600, 1600)
    ax.set_xlim(0, 5)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, mec='k', ms=20)
ax.grid(alpha=0.5)
ax.set_xlabel('time (s)')
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()

    if t >= xmax:
        ax.set_xlim(t, t+xmax)
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_stream, blit=False, interval=10,
                              repeat=True, init_func=init)
plt.show()

#s.close()