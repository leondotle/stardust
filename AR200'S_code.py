from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, time, os, system

# Define constants and variables.
BLACK = 35
SPEED = 30
CLAW_SPEED = 100
LINE_FOLLOW_DIRECTION = 15

is_turn = False
intersections = 0
lights = []
sun = ''

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

    global is_turn, intersections, BLACK
    if not is_turn and color_sensor.get_reflected_light() < BLACK:
        intersections += 1
        print("Intersections:", intersections)
        while not color_sensor.get_reflected_light() > BLACK:
            continue

def line_follow(color_sensor, condition):

    print('start line follow...')
    while condition:
        is_black = 1 if (color_sensor.get_reflected_light() < BLACK) else -1
        is_right = 1 if color_sensor == color_f else -1
        direction = is_black * is_right * LINE_FOLLOW_DIRECTION
        motor_pair.start(direction, speed = SPEED)
        if color_sensor == color_e:
            detect_intersection(color_f)
        else:
            detect_intersection(color_e)

def turn(position):

    global SPEED, is_turn
    yaw = hub.motion_sensor.get_yaw_angle() + 180
    if abs(position) > 1:
        is_turn = True
        if position > 0:
            motor_pair.start_tank(SPEED, 0 - SPEED)
        else:
            motor_pair.start_tank(0 - SPEED, SPEED)
        while (abs((hub.motion_sensor.get_yaw_angle() + 180) - ((yaw + (position % 360)) % 360)) > 1):
            continue
        motor_a.stop()
        motor_b.stop()
    is_turn = False

def claw(position):

    motor = Motor('C')
    motor.set_default_speed(10)
    if not motor.get_position() == position and position < 141 and position > -1:
        if motor.get_position() < 140 and motor.get_position() > position + 1:
            motor.run_to_position(position, direction = 'counterclockwise')
        else:
            motor.run_to_position(position, direction = 'clockwise')

def start():
    
    print('starting...')
    global SPEED
    sun = ''
    claw(90)
    motor_pair.set_default_speed(SPEED)
    motor_pair.move(10)
    claw(0)
    motor_pair.move(-10)
    turn(90)
    if int(distance_d.get_distance_cm()) < 10:
        sun = 'R'
    else:
        sun = 'L'
    motor_pair.set_default_speed(SPEED)
    motor_pair.stop()
    print(sun)
    turn(-90)
    return sun

def solar_panel_dropoff(sun):
    
    print('solar panel dropoff...')
    print(intersections)
    motor_pair.move(15)
    if sun == 'L':
        line_follow(color_f, intersections == 1)
    else:
        line_follow(color_e, intersections == 4)
    motor_pair.move(5)
    

def light_bulbs(dist):
    
    if light_bulbs_done():
        global lights, color_e, color_f
        move = None
        motor_pair.move(dist)
        claw(50)
        if color_e.get_color() == 'red' or color_e.get_color() == 'yellow':
            lights += [color_e.get_color()]
        elif color_f.get_color() == 'red' or color_f.get_color() == 'yellow':
            lights += [color_f.get_color()]
        move = True
        print(lights)
        if move:
            if lights[len(lights) - 1] == 'red':
                claw(90)
                motor_pair.move(10)
                claw(0)
                motor_pair.move(-10)
        claw(0)
        motor_pair.move(0 - dist)

def light_bulbs_done():
    global lights
    red == 0
    for item in lights:
        if item == 'red':
            red += 1
    return False if red >= 3 else True

def red_light_bulbs(sun):
    
    print('red light bulbs...')
    global lights

    if sun == 'R':
        turn(180)
        line_follow(color_e, intersections >= 6)
        motor_pair.move(5)
        turn(-180)
      
    motor_pair.move(-15)
    turn(90)
    light_bulbs(10)
    turn(-90)
    line_follow(color_e, intersections == 2)
    motor_pair.move(5)
    turn(90)
    light_bulbs(16.5)
    motor_pair.move(-5)
    turn(-90)
    line_follow(color_f, intersections == 3)
    motor_pair.move(5)
    turn(-90)
    light_bulbs(9)
    motor_pair.move(-5)
    turn(90)
    line_follow(color_e, intersections == 4)
    motor_pair.move(5)
    turn(90)
    light_bulbs(9)
    motor_pair.move(-5)
    turn(-90)
    line_follow(color_f, intersections == 5)
    motor_pair.move(5)
    turn(-90)
    light_bulbs(18.5)
    motor_pair.move(-5)
    turn(90)
    line_follow(color_e, intersections == 6)
    motor_pair.move(5)
    turn(90)
    light_bulbs(14)
    turn(-90)
    line_follow(color_e, intersections == 7)
    motor_pair.move(5)
    turn(90)
    line_follow(color_e, color_e.get_color() == 'red')
    claw(90)

def return_start():

    print('return start...')
    motor_pair.move(-20)
    claw(0)
    turn(90)
    motor_pair.move(5)
    turn(90)
    line_follow(color_f, intersections >= 8)
    motor_pair.move(5)
    turn(-90)
    line_follow(color_f, color_e.get_color() == 'white' or color_f.get_color() == 'white')

#Write your program here.
sun = start()
solar_panel_dropoff(sun)
red_light_bulbs(sun)
return_start()
