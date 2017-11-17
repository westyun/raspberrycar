#########################################################################
### Date: 2017/10/13
### file name: trackingModule.py
### Purpose: this code has been generated for the five-way tracking sensor
###         to perform the decision of direction
###
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
from go_any import *
from ultraModule import *
# =======================================================================
#  set GPIO warnings as false
# =======================================================================
GPIO.setwarnings(False)

# =======================================================================
# set up GPIO mode as BOARD
# =======================================================================
GPIO.setmode(GPIO.BOARD)

# =======================================================================
# declare the pins of 16, 18, 22, 40, 32 in the Rapberry Pi
# as the control pins of 5-way trackinmg sensor in order to
# control direction
#
#  leftmostled    leftlessled     centerled     rightlessled     rightmostled
#       16            18              22             40              32
#
# led turns on (1) : trackinmg sensor led detects white playground
# led turns off(0) : trackinmg sensor led detects black line

# leftmostled off : it means that moving object finds black line
#                   at the position of leftmostled
#                   black line locates below the leftmostled of the moving object
#
# leftlessled off : it means that moving object finds black line
#                   at the position of leftlessled
#                   black line locates below the leftlessled of the moving object
#
# centerled off : it means that moving object finds black line
#                   at the position of centerled
#                   black line locates below the centerled of the moving object
#
# rightlessled off : it means that moving object finds black line
#                   at the position of rightlessled
#                   black line locates below the rightlessled  of the moving object
#
# rightmostled off : it means that moving object finds black line
#                   at the position of rightmostled
#                   black line locates below the rightmostled of the moving object
# =======================================================================

leftmostled = 16
leftlessled = 18
centerled = 22
rightlessled = 40
rightmostled = 32

# =======================================================================
# because the connetions between 5-way tracking sensor and Rapberry Pi has been
# established, the GPIO pins of Rapberry Pi
# such as leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared whether their roles of pins
# are output pin or input pin
# since the 5-way tracking sensor data has been detected and
# used as the input data, leftmostled, leftlessled, centerled, rightlessled, and rightmostled
# should be clearly declared as input
#
# =======================================================================

GPIO.setup(leftmostled, GPIO.IN)
GPIO.setup(leftlessled, GPIO.IN)
GPIO.setup(centerled, GPIO.IN)
GPIO.setup(rightlessled, GPIO.IN)
GPIO.setup(rightmostled, GPIO.IN)

# =======================================================================
# GPIO.input(leftmostled) method gives the data obtained from leftmostled
# leftmostled returns (1) : leftmostled detects white playground
# leftmostled returns (0) : leftmostled detects black line
#
#
# GPIO.input(leftlessled) method gives the data obtained from leftlessled
# leftlessled returns (1) : leftlessled detects white playground
# leftlessled returns (0) : leftlessled detects black line
#
# GPIO.input(centerled) method gives the data obtained from centerled
# centerled returns (1) : centerled detects white playground
# centerled returns (0) : centerled detects black line
#
# GPIO.input(rightlessled) method gives the data obtained from rightlessled
# rightlessled returns (1) : rightlessled detects white playground
# rightlessled returns (0) : rightlessled detects black line
#
# GPIO.input(rightmostled) method gives the data obtained from rightmostled
# rightmostled returns (1) : rightmostled detects white playground
# rightmostled returns (0) : rightmostled detects black line
#
# =======================================================================
pwm_setup()
n=7
rl = 0
signal = int(input())
try:
    while 1:
        list =[(GPIO.input(leftmostled)), (GPIO.input(leftlessled)), (GPIO.input(centerled)), (GPIO.input(rightlessled)), (GPIO.input(rightmostled))]
        if list == [1, 1, 1, 1, 1] or list == [1, 1, 0, 1, 1] or list == [1, 0, 0, 0, 1] or list == [1, 1, 0, 0, 1] or list == [1, 0, 0, 1, 1]:
            if (n % 10) == 0:
                print(getDistance())
                if getDistance() < 50:
                    if signal == 0:
                        right_point_turn(50, 50)
                        sleep(0.2)
                        trace_any(45, 45)
                        sleep(2)
                        left_point_turn(70, 70)
                        sleep(0.8)
                        while 1:
                            trace_any(45, 45)
                            sleep(0.01)
                            if list == [1, 1, 0, 1, 1] or list == [1, 1, 1, 0, 1] or list == [1, 1, 1, 1, 0]:
                                break
                    else:
                        left_point_turn(50, 50)
                        sleep(0.2)
                        trace_any(45, 45)
                        sleep(2)
                        right_point_turn(70, 70)
                        sleep(0.8)
                        while 1:
                            trace_any(45, 45)
                            sleep(0.01)
                            if list == [1, 1, 0, 1, 1] or list == [1, 0, 1, 1, 1] or list == [0, 1, 1, 1, 1]:
                                break
            if list == [1, 1, 1, 1, 1] or list == [1, 1, 0, 1, 1] or list == [1, 0, 0, 0, 1]:
                trace_any(45, 45)
            elif list == [1, 0, 0, 1, 1]:
                trace_any(50, 35)
                print('rightlowest')
            elif list == [1, 1, 0, 0, 1]:
                trace_any(50, 35)
                print('leftlowest')
            n += 1
        elif list == [0, 1, 1, 1, 1]:
            print('leftmost')
            left_point_turn(5, 90)
        elif list == [1, 1, 1, 1, 0]:
            print('rightmost')
            right_point_turn(90, 5)
        elif list == [1, 1, 1, 0, 0]:
            trace_any(65, 10)
        elif list == [0, 0, 1, 1, 1]:
            trace_any(10, 65)
        elif list == [1, 0, 1, 1, 1]:
            trace_any(15 ,55)
            print('rightlittle')
        elif list == [1, 1, 1, 0, 1]:
            trace_any(55 ,15)
            print('leftlittle')
        elif list == [0 ,0, 0, 0, 0]:
            GPIO.cleanup()
            exit()
        sleep(0.005)
except KeyboardInterrupt:
    GPIO.cleanup()
