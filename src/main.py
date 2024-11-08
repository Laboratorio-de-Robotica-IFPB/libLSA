#!/usr/bin/env pybricks-micropython
import sys

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

lsa = LSA(Port.S4)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

'''
kp = 5
base_speed = 90
weights = [-4, -3, -2, -1, 1, 2, 3, 4]

def weight_average():
    weightedSum = 0
'''
flag = False
while True:
    buttons = ev3.buttons.pressed()
    sv = lsa.read_calibrated()

    print("leitura do sensor: ", sv)

    left_motor.run(300)
    right_motor.run(300)
    
    if sv == bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00'):
        ev3.speaker.beep()
        left_motor.stop()
        right_motor.stop()
        wait(1000)
    
    if Button.UP in buttons:
        lsa.issueCommand('W')
        wait(1000)

    if Button.DOWN in buttons:
        lsa.issueCommand('B')
        wait(1000)
    '''
    print("limite do branco: ", limit_b)
    print("calibração do branco: ", cb)
    print("limite do preto: ", limit_p)
    print("calibração do preto: ", cp)


    center = (v[3] + v[4]) * 0.5 

    left = (v[0] + v[1] + v[2]) / 3

    right = (v[5] + v[6] + v[7]) / 3

    error = 0 - center 

    output = kp * error

    left_speed  = base_speed + output
    right_speed = base_speed - output

    left_motor.run(left_speed)
    right_motor.run(right_speed)
    '''