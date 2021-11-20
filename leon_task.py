from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
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
    motorpair.move(MathYuanGod,'cm',speed=30)
def LineFollow(stopAt):
    print("-----------------------")
    print("Starting line following")
    print("-----------------------")
    passed_lines = 0
    print("passed lines: " + str(passed_lines))
    start = 0
    while passed_lines < stopAt:
        turn_rate = (color.get_reflected_light() -70 * 0.7)
        motorpair.start(steering=int(turn_rate), speed = 30)
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
    motorpair.move(-0.15,speed=30)
    motorpair.move_tank(dis, 'cm', left_speed=30, right_speed=-30)
def LiftClaw(amount):
    motor.run_for_rotations(amount, speed=30)
'''Move(10)
LineFollow(2)
Move(-3)
TurnRight(12)
LiftClaw(0.4)
Move(20)
Move(5)
LiftClaw(-0.4)
Move(-25)
TurnRight(-12)
Move(7)
LiftClaw(0.4)
TurnRight(-12)
Move(19)
LiftClaw(-0.4)
Move(-19)
TurnRight(12)
LineFollow(4)
TurnRight(-12)'''
Move(30)
LiftClaw(0.4)
Move(-33)
LiftClaw(-0.4)
TurnRight(-12)
Move(5)
LineFollow(1)
TurnRight(-12)
LiftClaw(0.4)
Move(16)
Move(3)
LiftClaw(-0.4)
Move(-19)
TurnRight(12)
LineFollow(4)
TurnRight(-12)
LiftClaw(0.4)
Move(13)
Move(4)
LiftClaw(-0.4)
Move(-17)
TurnRight(12)
LineFollow(1)
TurnRight(12)
Move(30)
TurnRight(-12)
Move(10)
LiftClaw(0.4)
Move(-10)
