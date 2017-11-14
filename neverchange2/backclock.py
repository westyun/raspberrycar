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
# import getDistance() method in the ultraModule
# =======================================================================
from ultraModule import getDistance

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
from condition import *

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
dis = 20  # ??
case = 1

try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        ledcondition = gettracking()
        print('distance= ', distance)
        print(ledcondition)
        
        # when the distance is above the dis, moving object forwards
        if (distance > dis) and (ledcondition in forward_condition) and (case ==1):
            go_forward(40,0.3)
            stop()
            sleep(0.1)
        elif (distance > dis) and (ledcondition in sp1) and (case ==1):
            curveturn(20,30,0.5)
            stop()
            sleep(0.5)
        elif (distance > dis) and (ledcondition in sp2) and (case ==1):
            curveturn(30,20,0.5)
            stop()
            sleep(0.5)

        elif (distance <= dis):
            stop()
            sleep(0.5)
            rightSwingTurn(40,0.5)
            go_forward(90,0.1)
            leftSwingTurn(40,0.5)
            go_forward(90,0.1)
            leftSwingTurn(40,0.5)
            case +=1
            if (distance > dis) and (ledcondition in keep_condition):
                go_forward_any(50)
            else:
                stop()
                sleep(0.5)
                rightSwingTurn(40,0.5)
        while (distance > dis) and (ledcondition in left_condition) and (case ==2):
            curveturn(20,30,1)
                
            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()
