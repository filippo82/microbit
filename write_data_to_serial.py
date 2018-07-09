from microbit import *
import math

REFRESH = 50


def get_data():
    x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
    #acceleration = math.sqrt(x**2 + y**2 + z**2)
    #a, b = button_a.was_pressed(), button_b.was_pressed()
    #print(x, y, z, a, b)
    print(x, y, z)


def run():
    while True:
        sleep(REFRESH)
        get_data()


display.show('S')

run()