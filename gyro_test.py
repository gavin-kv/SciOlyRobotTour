#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    GyroSensor,
)
from pybricks.nxtdevices import (
    UltrasonicSensor
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

right_motor = Motor(Port.B)
left_motor = Motor(Port.C)
ultrasonic = UltrasonicSensor(Port.S2)
gyro = GyroSensor(Port.S3)
touch_sensor = TouchSensor(Port.S4)
path_map = []
time = 0

while True:
    ev3.screen.print(ultrasonic.distance())
    print(ultrasonic.distance())