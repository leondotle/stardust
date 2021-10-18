from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, time, os, system

# Define constants and variables.
BLACK = 40
SPEED = 15
CLAW_SPEED = 100
LINE_FOLLOW_DIRECTION = 20

turn = False
intersections = 0
lights = []

# Create your objects here.
hub = MSHub()
motor_a = Motor('A')
motor_b = Motor('B')
motor_c = Motor('C')
distance_d = DistanceSensor('D')
motor_pair = MotorPair('A', 'B')
color_e = ColorSensor('E')
color_f = ColorSensor('F')

# Create your functions here.
def detect_intersection(color_sensor):
    global turn, intersections
    if not Turn and color_sensor.get_reflected_light() < BLACK:
        intersections += 1
        print("Intersections:", intersections)
        while not color_sensor.get_reflected_light() > BLACK:
            continue

def line_follow(color_sensor, direction):
    is_black = 1 if (color_sensor.get_reflected_light() < BLACK) else -1
    is_right = 1 if direction == 'R' else -1
    direction = is_black * is_right * LINE_FOLLOW_DIRECTION
    motor_pair.start(direction, speed = SPEED)

def turn(position):
    global SPEED, turn
    yaw = hub.motion_sensor.get_yaw_angle() + 180
    if abs(position) > 1:
        Turn = True
        if position > 0:
            motor_pair.start_tank(SPEED, 0 - SPEED)
        else:
            motor_pair.start_tank(0 - SPEED, SPEED)
        while (abs((hub.motion_sensor.get_yaw_angle() + 180) - ((yaw + (position % 360)) % 360)) > 1):
            continue
        motor_a.stop()
        motor_b.stop()
    Turn = False

def claw(position):
    motor = Motor('C')
    motor.set_default_speed(10)
    if not motor.get_position() == position and position < 141 and position > -1:
        if motor.get_position() < 140 and motor.get_position() > position + 1:
            motor.run_to_position(position, direction = 'counterclockwise')
        else:
            motor.run_to_position(position, direction = 'clockwise')

def start():
    claw(90)
    motor_pair.set_default_speed(SPEED)
    motor_pair.move(10)
    claw(0)
    motor_pair.move(-10)
    turn(90)
    solar_panel()
    turn(-90)

def solar_panel():
    if distance_d.get_distance_cm() < 10:
        sun = 'R'
    else:
        sun = 'L'
        if distance_d.get_distance_cm() > 4:
            motor_pair.start()
        motor_pair.stop()
    if sun == 'L':
        turn(-90)
        motor_pair.move(20)
        while intersections < 1:
            line_follow(color_f, 'R')
            detect_intersection(color_e)
        motor_pair.move(5)
        turn(-90)
        while intersections < 1:
            line_follow(color_f, 'R')
        while intersections < 2:
            line_follow(color_e, 'L')
            motor_pair.start()
            detect_intersection(color_e)
            detect_intersection(color_f)
            motor_pair.stop()
    else:
        turn(-90)
        motor_pair.move(20)
        while intersections < 4:
            line_follow(color_e, 'L')
            detect_intersection(color_f)
        motor_pair.move(5)
        turn(90)
        while distance_d.get_distance_cm() != 4:
            motor_pair.move(6, 'cm')
            turn(90)
            claw(90)
            motor_pair.move(2, 'cm')
            motor_pair.move(-16, 'cm')
        turn(90)
        while intersections < 5:
            line_follow(color_f, 'R')
            motor_pair.start()
            detect_intersection(color_e)
            detect_intersection(color_f)
            motor_pair.stop()
    return sun

def light_bulbs(dist):
    global lights
    motor_pair.move(dist)
    claw(50)
    if color_e.get_color() == 'red' color_e.get_color() == 'yellow':
        lights += [color_e.get_color()]
    if color_f.get_color() == 'red' color_f.get_color() == 'yellow':
        lights += [color_f.get_color()]
    if lights[len(lights) - 1] == 'red':
        claw(90)
        motor_pair.move(10)
        claw(0)
        motor_pair.move(-10)
    motor_pair.move(0 - dist)

def red_light_bulbs(sun):
    global lights
    if sun == 'L':
        light_bulbs(10)
        turn(-90)
        while intersections < 3:
            line_follow(color_e, 'L')
            detect_intersections(color_f)
        motor_pair.move(5)
        turn(90)
        light_bulbs(14)
        motor_pair.move(-5)
        turn(-90)
        while intersections < 4:
            line_follow(color_f, 'R')
        motor_pair.move(5)
        turn(-90)
        light_bulbs(8)
        motor_pair.move(-5)
        turn(90)
        while intersections < 5:
            line_follow(color_e, 'L')
    else:
        asasdfasdfasldkfjas;ldkjf;sladkjfa;lskdjf;lksjflkadskflsakdjfl;kdskfasfkasfdfjsadf

def white_light_bulbs():
    pass
    None

#Write your program here.
start()
for light in range(6):
    red_light_bulbs(solar_panel())
