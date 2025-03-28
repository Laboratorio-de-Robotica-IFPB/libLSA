#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import Font
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from mindsensorsPYB import LSA

font = Font(size=6)

ev3 = EV3Brick()
ev3.screen.set_font(font)

lsa = LSA(Port.S3)

#left_motor = Motor(Port.B)
#right_motor = Motor(Port.C)


while True:
    buttons = ev3.buttons.pressed()
    sv = lsa.read_calibrated()
    
    if Button.UP in buttons:
        lsa.calibrate_white()
        wait(1000)
        print("White Limit is sucessfully calibrated")

    if Button.DOWN in buttons:
        lsa.calibrate_black()
        wait(1000)
        print("Black Limit is sucessfully calibrated")

    print("leitura do sensor: ", sv)

    #left_motor.run(300)
    #right_motor.run(300)
    
    if sv == bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00'):
        ev3.speaker.beep()
        #left_motor.stop()
        #right_motor.stop()
        wait(1000)
    
