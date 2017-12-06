######################################################################
### Date: 2017/10/5
### file name: project3_student.py
### Purpose: this code has been generated for the three-wheeled moving
###         object to perform the project3 with ultra sensor
###         swing turn, and point turn
### this code is used for the student only
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
from time import sleep

# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# import TurnModule() method
# =======================================================================
from TurnModule import *
from trackingModule import gettracking

# =======================================================================
# rightPointTurn() and leftPointTurn() in TurnModule module
# =======================================================================
# student assignment (1)
# student assignment (2)



# =======================================================================
# import go_forward_any(), go_backward_any(), stop(), LeftPwm(),
# RightPwm(), pwm_setup(), and pwm_low() methods in the module of go_any
# =======================================================================
from go_any import *
from condition2 import *

# implement rightmotor(x)  # student assignment (3)
# implement go_forward_any(speed): # student assignment (4)
# implement go_backward_any(speed): # student assignment (5)
# implement go_forward(speed, running_time)  # student assignment (6)
# implement go_backward(speed, running_time)  # student assignment (7)

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================
pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  to perform the project3 with ultra sensor
#  and swing turn
# =======================================================================
leftSwingTurn(5,0.1)
print('motorInitialize')
try:
    while True:
        # ultra sensor replies the distance back
        ledcondition = gettracking()
        print(ledcondition)
        if ledcondition in forward:
            go_forward(30,0.3)
            print(1)
        elif ledcondition in sp1:
            curveturn(20,35,0.1)
            print(2)
        elif ledcondition in sp2:
            curveturn(35,20,0.1)
            print(3)
            
        if ledcondition in rightturn:
            print("rightturn forward")
            go_forward(50,0.53)
            stop()
            print("RIGHTTURN")
            stop()
            sleep(1)
            right_point_turn(40,0.25)
            stop()
            sleep(1)
            con =0
            
        if ledcondition in allline:
            print(ledcondition)
            print('all line')
            con =0
            con2 = 1
            go_forward(50,0.15)
            stop()
            sleep(1)
            print("allLine forward")
            if ledcondition in forward:
                right_point_turn(40,0.1)

        if ledcondition in leftturn or leftturn2:
            print("leftturn forward")
            go_forward(50,0.45)
            stop()
            print("lefTTURN")
            stop()
            sleep(3)
            left_point_turn(40,0.25)
            stop()
            sleep(3)
            con = 1
            
        if ledcondition in noline:
            if con == 0:
                print("no line")
                right_point_turn(40,0.1)
                stop()
                sleep(0.2)
            elif con ==1:
                print("no line 2 ")
                left_point_turn(40,0.1)
                stop()
                sleep(0.2)
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped 

except KeyboardInterrupt:
    pwm_low()
