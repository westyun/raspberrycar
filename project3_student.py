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
from trackingModule import ledcondition

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
obstacle = 1

# when obstacle=1, the power and
# running time of the first turn
SwingPr = 90  # student assignment (8)
SwingTr = 0.9  # student assignment (9)

try:
    while True:
        # ultra sensor replies the distance back
        distance = getDistance()
        print('distance= ', distance)

        if (distance > dis) and (ledcondition in forward_condition):
            go_forward_any(50)

        else:
            stop()
            sleep(1)

        rightswingturn(50, 2)
        stop()
        sleep(1)
        go_forward(50, 2)
        stop()
        sleep(1)
        leftswingturn(50, 2)
        stop()
        sleep(1)
        go_forward(50, 2)
        stop()
        sleep(1)
        leftswingturn(50, 2)
        stop()
        sleep(1)
        go_forward_any(50)

        if ledcondition not in keep_condition:
            stop()
            sleep(1)
        rightswingturn(50,2)

        if (distance > dis) and (ledcondition in forward_condition):
            go_forward_any(50)

        else:
            stop()
            sleep(1)

        while True:
            if ledcondition in left_condition:
                curveturn(50,80,1)
            else:
                break

            ########################################################
            ### please continue the code or change the above code
            ### # student assignment (10)
            ########################################################


# when the Ctrl+C key has been pressed,
# the moving object will be stopped

except KeyboardInterrupt:
    pwm_low()