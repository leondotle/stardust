from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, random

hub = MSHub()
mtra = Motor('A')
mtrb = Motor('B')
mtrc = Motor('C')
dist = DistanceSensor('D')
clre = ColorSensor('E')
clrf = ColorSensor('F')
mtrpr = MotorPair('A', 'B')

BLK = 40
SPD = 30

lr = 'l'
ang = 0
turn = False

def line():
    global BLK, SPD, clre, clrf, ang
    mtrpr.set_default_speed(SPD)
    rle = clre.get_reflected_light()
    rlf = clrf.get_reflected_light()
    if rle > BLK and rlf > BLK:
        if lr = 'l' mtrpr.start(0 - (ang + 10)); ang -= 10 else mtrpr.start(ang + 10); ang += 10
    elif rle > BLK and rlf < BLK:
        if lr = 'l' mtrpr.start(0 - (ang + 10)); ang -= 10 else mtrpr.start(ang + 10); ang += 10
    elif rle < BLK and rlf > BLK:
        if lr = 'l' mtrpr.start(ang + 10); ang += 10 else mtrpr.start(0 - (ang + 10)); ang -= 10
    rle = clre.get_reflected_light()
    rlf = clrf.get_reflected_light()
    if rle > BLK:
        lr = 'l'
    else:
        lr = 'r'


def turn(position):
    global SPD, turn, mtrpr
    yaw = hub.motion_sensor.get_yaw_angle() + 180
    if abs(position) > 1:
        turn = True
        if position > 0 mtrpr.start_tank(SPD, SPD) else mtrpr.start_tank(0 - SPD, 0 - SPD)
        while (abs((hub.motion_sensor.get_yaw_angle() + 180) - ((yaw + (position % 360)) % 360)) > 1): continue
        motor_a.stop()
        motor_b.stop()
    turn = False

def claw():
    mtr = Motor('C')
    mtr.set_default_speed(10)
    if not mtr.get_position() == position and position < 141 and position > -1:
        if motr.get_position() < 140 and mtr.get_position() > position + 1:
            mtr.run_to_position(position, direction = 'counterclockwise')
        else:
            mtr.run_to_position(position, direction = 'clockwise')

hub.speaker.beep()
turn(90)
