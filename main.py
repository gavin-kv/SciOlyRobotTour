#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor,
    TouchSensor,
    ColorSensor,
    InfraredSensor,
    UltrasonicSensor,
    GyroSensor,
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
gyro = GyroSensor(Port.S3)
touch_sensor = TouchSensor(Port.S1)
path_map = []
time = 0


def rightTurn():
    gyro.reset_angle(0)
    right_motor.dc(-25)
    left_motor.dc(25)
    while gyro.angle() < 85:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(250)


def leftTurn():
    gyro.reset_angle(0)
    right_motor.dc(25)
    left_motor.dc(-25)
    while gyro.angle() > -85:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(250)


def forward(desp):
    left_motor.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.dc(desp)
    left_motor.dc(desp)
    while left_motor.angle() < 885:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(250)


def f():
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    right_motor.dc(25)
    left_motor.dc(25)
    while left_motor.angle() < 540:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(250)


def updateConfig():
    time = 50
    path_map.append("RT")
    path_map.append("F")
    path_map.append("LT")
    path_map.append("F")
    path_map.append("RT")
    path_map.append("F")
    path_map.append("LT")
    path_map.append("F")
    path_map.append("LT")
    path_map.append("F")
    path_map.append("RT")
    path_map.append("F")
    path_map.append("RT")
    path_map.append("RT")
    path_map.append("F")
    path_map.append("RT")
    path_map.append("F")
    path_map.append("F")
    path_map.append("RT")
    path_map.append("F")
    path_map.append("RT")
    path_map.append("F")


# Write your program here.
updateConfig()
while not touch_sensor.pressed():
    wait(100)

forwards = 0
time -= 2.4

for entry in path_map:
    if entry == "RT" or entry == "LT":
        time -= 1.1
    elif entry == "F":
        forwards += 1

tperf = time / forwards
despw = 50.0

mindif = min(abs(tperf - 5.4), abs(tperf - 3.8), abs(tperf - 2.4), abs(tperf - 2.1))
if mindif == abs(tperf - 5.4):
    despw = 17.5
elif mindif == abs(tperf - 3.8):
    despw = 25
elif mindif == abs(tperf - 2.4):
    despw = 42.5
elif mindif == abs(tperf - 2.1):
    despw = 50

f()
for instruction in path_map:
    if instruction == "RT":
        rightTurn()
    elif instruction == "LT":
        leftTurn()
    elif instruction == "F":
        forward(despw)
