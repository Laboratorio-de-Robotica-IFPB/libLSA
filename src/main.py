#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
#from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import Font
from mindsensorsPYB import LSA

ev3 = EV3Brick()
lsa = LSA(Port.S4)
ev3.screen.set_font(Font(size=8))

while True:

    v = lsa.read_calibrated()
    print(v)