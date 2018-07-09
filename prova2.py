#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 00:14:14 2018

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

def data_stream(t=0):
    cnt = 0
    while True: #cnt < 1000:
        cnt += 1
        t += 0.1
        data = s.readline().decode('UTF-8')
        data_s = data.rstrip().split(' ')
        try:
            x, y, z = list(map(float, data_s))
#            a, b = data_s[3:5]
#            print(t, cnt, x, y, z, a, b)
#            print(type(x))
        except:
            pass
        
        yield t, x, y, z


def init():
    ax.set_ylim(-1200, 1200)
    ax.set_xlim(0, 10)
#    del xdata[:]
#    del ydata[:]
    linex.set_data(tdata, xdata)
    liney.set_data(tdata, ydata)
    linez.set_data(tdata, zdata)
    return linex, liney, linez

fig, ax = plt.subplots()
linex, = ax.plot([], [], lw=2, mec='k', ms=20)
liney, = ax.plot([], [], lw=2, mec='k', ms=20)
linez, = ax.plot([], [], lw=2, mec='k', ms=20)
ax.grid(alpha=0.5)
ax.set_xlabel('time (s)')
tdata, xdata, ydata, zdata = [], [], [], []
#tdata = []

def run(data):
    # update the data
    t, x, y, z = data

    xmin, xmax = ax.get_xlim()
    if t >= xmax:
        ax.set_xlim(t, t+10)
        ax.figure.canvas.draw()
        del tdata[:]
        del xdata[:]
        del ydata[:]
        del zdata[:]
    
    tdata.append(t)
    xdata.append(x)
    ydata.append(y)
    zdata.append(z)
    print(len(tdata))
#    xmin, xmax = ax.get_xlim()

#    if t >= xmax:
#        ax.set_xlim(t, t+10)
#        ax.figure.canvas.draw()
#        tdata, xdata, ydata, zdata = [], [], [], []
        
    linex.set_data(tdata, xdata)
    liney.set_data(tdata, ydata)
    linez.set_data(tdata, zdata)

    return linex, liney, linez

ani = animation.FuncAnimation(fig, run, data_stream, blit=True, interval=50,
                              repeat=True, init_func=init)
plt.show()

#s.close()