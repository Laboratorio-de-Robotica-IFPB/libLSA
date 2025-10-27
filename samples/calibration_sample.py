#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.media.ev3dev import Font
from pybricks.tools import wait
from mindsensorsPYB import LightSensorArray

ev3 = EV3Brick()
ev3.screen.set_font(Font(size=6))

lsa = LightSensorArray(Port.S4)

#left_motor = Motor(Port.B)
#right_motor = Motor(Port.C)

while True:
    buttons = ev3.buttons.pressed()
    current_reading = lsa.read_calibrated()
    
    if Button.UP in buttons:
        lsa.calibrate_white()
        wait(1000)
        print("White Limit is sucessfully calibrated")

    if Button.DOWN in buttons:
        lsa.calibrate_black()
        wait(1000)
        print("Black Limit is sucessfully calibrated")

    print("Sensor Output: ", current_reading)
