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
ultrasonic = UltrasonicSensor(Port.S2)
gyro = GyroSensor(Port.S3)
touch_sensor = TouchSensor(Port.S4)
path_map = []
time = 0

# <0 - Left
# >0 - Right

# Smart Moving Forward - move (smart) until < 250 && > 100


def rightTurn():
    gyro.reset_angle(0)
    right_motor.dc(-50)
    left_motor.dc(50)
    while gyro.angle() < 60:
        wait(10)
    right_motor.dc(-20)
    left_motor.dc(20)
    while gyro.angle() < 80:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(500)


def oneEighty():
    gyro.reset_angle(0)
    right_motor.dc(-50)
    left_motor.dc(50)
    while gyro.angle() < 150:
        wait(10)
    right_motor.dc(-20)
    left_motor.dc(20)
    while gyro.angle() < 170:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(500)


def leftTurn():
    gyro.reset_angle(0)
    right_motor.dc(50)
    left_motor.dc(-50)
    while gyro.angle() > -60:
        wait(10)
    right_motor.dc(20)
    left_motor.dc(-20)
    while gyro.angle() > -80:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(500)


def forward(desp):
    gyro.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    right_motor.dc(desp)
    left_motor.dc(desp)
    while left_motor.angle() < 865:
        right_motor.dc(desp)
        left_motor.dc(desp)
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(500)


def wall(desp):
    gyro.reset_angle(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    right_motor.dc(desp)
    left_motor.dc(desp)
    while ultrasonic.distance() > 90:
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


def f():
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    right_motor.dc(25)
    left_motor.dc(25)
    while left_motor.angle() < 450:
        wait(10)
    right_motor.hold()
    left_motor.hold()
    wait(250)


""" 
R - Right turn    
L - Left Turn   
S - Straight (50cm)     
F - Straight (25cm)     
U - U-Turn
W - Forward to the next wall
"""


def updateConfig():
    time = 59
    path_map.append("R")
    path_map.append("S")
    path_map.append("S")
    path_map.append("L")
    path_map.append("S")
    path_map.append("U")
    path_map.append("S")
    path_map.append("L")
    path_map.append("S")
    path_map.append("L")
    path_map.append("S")
    path_map.append("S")
    path_map.append("L")
    path_map.append("S")
    path_map.append("R")
    path_map.append("S")
    path_map.append("L")
    path_map.append("S")
    path_map.append("S")


# Write your program here.
updateConfig()
while not touch_sensor.pressed():
    wait(50)

forwards = 0
time -= 2.4

for entry in path_map:
    if entry == "R" or entry == "L":
        time -= 1.1
    elif entry == "U":
        time -= 2.2
    elif entry == "S":
        forwards += 1
    elif entry == "W":
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
    if instruction == "R":
        rightTurn()
    elif instruction == "L":
        leftTurn()
    elif instruction == "S":
        forward(despw)
    elif instruction == "F":
        f()
    elif instruction == "U":
        oneEighty()
    elif instruction == "W":
        wall(despw)
