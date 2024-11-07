#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from mindsensorsPYB import LSA

ev3 = EV3Brick()
lsa = LSA(Port.S1)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

kp = 5
base_speed = 30

while True:
    v = lsa.read_calibrated()
    
    center = (v[3] + v[4]) * 0.5 

    left = (v[0] + v[1] + v[2]) / 3

    right = (v[5] + v[6] + v[7]) / 3

    error = 0 - center 

    output = kp * error

    left_speed  = base_speed + output
    right_speed = base_speed - output

    left_motor.run(left_speed)
    right_motor.run(right_speed)