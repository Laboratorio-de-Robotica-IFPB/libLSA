#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.media.ev3dev import Font
from mindsensorsPYB import LSA

ev3 = EV3Brick()
lsa = LSA(Port.S1)

ev3.screen.set_font(Font(size=8))
ev3.speaker.beep()

ev3.screen.print("Firmware: ", lsa.GetFirmwareVersion())
ev3.screen.print("VendorID: ", lsa.GetVendorName())
ev3.screen.print("DeviceID: ", lsa.GetDeviceId())

while True:
    breakOut = Button.CENTER in ev3.buttons.pressed()

    if breakOut:
        break

    values = lsa.ReadRaw_Uncalibrated()
    ev3.screen.print(values)
