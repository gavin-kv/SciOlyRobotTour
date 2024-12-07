#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    GyroSensor,
    UltrasonicSensor,
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


def wall(desp):
    gyro.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    right_motor.dc(desp)
    left_motor.dc(desp)
    while ultrasonic.distance() > 90:
        ev3.screen.print(ultrasonic.distance())
        print(ultrasonic.distance())
        if gyro.angle() > 3:
            right_motor.dc(desp + 10)
            left_motor.dc(desp)
        elif gyro.angle() < -3:
            right_motor.dc(desp)
            left_motor.dc(desp + 10)
        else:
            right_motor.dc(desp)
            left_motor.dc(desp)
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(500)


def rightTurn():
    gyro.reset_angle(0)
    right_motor.dc(-50)
    left_motor.dc(50)
    while gyro.angle() < 60:
        wait(10)
    right_motor.dc(-20)
    left_motor.dc(20)
    while gyro.angle() < 85:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(500)


wall(50)
rightTurn()
