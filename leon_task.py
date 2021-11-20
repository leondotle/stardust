from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
app = App()
timer = Timer()
motorpair = MotorPair('A', 'B')
color = ColorSensor('C')
hub = MSHub()
motor=Motor('E')
def Move(MathYuanGod):
    motorpair.move(MathYuanGod,'cm',speed=20)
def LineFollow(stopAt):
    print("-----------------------")
    print("Starting line following")
    print("-----------------------")
    passed_lines = 0
    print("passed lines: " + str(passed_lines))
    start = 0
    while passed_lines < stopAt:
        turn_rate = (color.get_reflected_light() -70 * 0.7)
        motorpair.start(steering=int(turn_rate), speed = 20)
        if ColorSensor('D').get_reflected_light() < 40:
            if timer.now() > 1:
                passed_lines += 1
                timer.reset()
                print("^^^^^^^^^^^^^^^^^^^")
                print("passed lines: " + str(passed_lines))
                print("^^^^^^^^^^^^^^^^^^^")
            else:
                print("!!!!!!!!!!!!!!!!!!!!")
                print("LINE ERROR/WEIRD ERROR MESSEGE THAT I CANNOT GET TO WORK")
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
    motorpair.move(-0.15,speed=10)
    motorpair.move_tank(dis, 'cm', left_speed=30, right_speed=-30)
def Detector(amount):
    TurnRight(12)
    wait_for_seconds(2)
    motor.run_for_rotations(0.15,speed=10)
    motorpair.move(amount,'cm',speed=10)
    wait_for_seconds(2)
    if ColorSensor('D').get_color() == 'red' or ColorSensor('C').get_color() == 'red':
        motor.run_for_rotations(0.15, speed=10)
        Move(7)
        motor.run_for_rotations(-0.3, speed=10)
        Move(-7)
        motorpair.move(-amount, 'cm',speed=10)
    else:
        motorpair.move(-amount/2, 'cm',speed=10)
        motor.run_for_rotations(-0.15, speed=10)
        motorpair.move(-amount/2, 'cm', speed=10)
LineFollow(1)
Detector(11)
TurnRight(-12)
LineFollow(1)
Detector(17)
TurnRight(-12)
LineFollow(1)
Detector(12)
TurnRight(-12)
LineFollow(2)
Detector(15)
TurnRight(-12)
LineFollow(1)
TurnRight(12)
Move(50)
motor.run_for_rotations(0.4,speed=10)
Move(-55)
motor.run_for_rotations(-0.4,speed=10)
TurnRight(12)
LineFollow(2)
Detector(11)
TurnRight(-12)
LineFollow(1)
Detector(11)
TurnRight(12)
LineFollow(3)
TurnRight(-12)
Move(30)
motor.run_for_rotations(0.4,speed=10)
Move(-30)
motor.run_for_rotations(-0.4,speed=1)
