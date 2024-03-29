from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
timer = Timer()
motorpair = MotorPair('A', 'B')
color = ColorSensor('C')
hub = MSHub()
motorpair.set_default_speed(20)

def LineFollow(stopAt):
    print("-----------------------")
    print("Starting line following")
    print("-----------------------")
    passed_lines = 0
    print("passed lines: " + str(passed_lines))
    start = 0
    while passed_lines < stopAt:
        motorpair.start(color.get_reflected_light() - 50)
        #motorpair.start_tank(int(40+0.3 * turn_rate), int(40-0.3 * turn_rate))
        if ColorSensor('D').get_reflected_light() < 30:
            if timer.now() > 1:
                passed_lines += 1
                timer.reset()
                print("^^^^^^^^^^^^^^^^^^^")
                print("passed lines: " + str(passed_lines))
                print("^^^^^^^^^^^^^^^^^^^")
            else:
                print("!!!!!!!!!!!!!!!!!!!!")
                print("WROasted")
                print("TYPEERROR")
                print("!!!!!!!!!!!!!!!!!!!!")
    print("************************")
    print("Line follow fininshed!!")
    print("************************")
    if passed_lines == stopAt:
        motorpair.stop()

def TurnRight(dis):
    print("************************")
    print("Turn Right!")
    print("************************")
    motorpair.move_tank(dis, 'cm', left_speed=30, right_speed=-30)
def RedPickUp():
    print("************************")
    print("Pick Up!")
    print("************************")
    motor = Motor('E')
    motor.run_for_rotations(-0.8, speed=10)
    motorpair.move(13, 'cm', speed=10)
    wait_for_seconds(2)
    if ColorSensor('D').get_color() == 'red':
        motor.run_for_rotations(1, speed=10)
        motorpair.move(-13, 'cm',speed=10)
    else:
        motorpair.move(-13, 'cm',speed=10)
        motor.run_for_rotations(1, speed=10)
'''        motorpair.move(-3, 'cm')
        TurnRight(-16)
        motor.run_for_rotations(1, speed=10)
        LineFollow(2)'''
LineFollow(1)
motorpair.move(2,'cm',speed=10)
TurnRight(8)
RedPickUp()
TurnRight(-8)
LineFollow(5)
TurnRight(8)
motorpair.move(40, 'cm', speed=10)
motor=Motor('E')
motor.run_for_rotations(-0.8,speed=10)
