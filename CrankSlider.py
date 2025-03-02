###############################
'''
# Author: Matthew Ryan Liqua
# Created Date: 2/22/25
# Last Edited Date: 3/1/25
# Course: ENGR Mech Design
# Purpose: Calcuates postion, velocity, and accleration
			of crank slider mechanism
'''
####################################################

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

print("\n")
print("This calculation assumes ground is d [R1] and theta4 = 90")
print("Recall that any -d [R1] value means it is an non-real circuit")
print("Ensure that all units for length are the same.")
a = float(input("Input a [R2] length: "))
b = float(input("Input b [R3] length: "))
c = float(input("Input c [R4] length: "))
theta2 = radians(float(input("Input theta 2 (degree): ")))
print("\n")

####################################################
# First theta 3 value

OutTheta3_1 = asin( ((a * sin(theta2) - c) / b) )
print("Theta 3_1 value is: ", round(degrees(OutTheta3_1),2))

OutD_1 = a*cos(theta2) - b*cos(OutTheta3_1)
print("d_1 [R1] value is:", round(OutD_1, 2))
if OutD_1 > 0:
	print("This is the real circuit.")
else:
	print("This is the non-real circuit.")
print("\n")

####################################################
# Second theta 3 value
# asin is a multi valued function, hence OutTheta3_2
OutTheta3_2 = asin( - ((a * sin(theta2) - c) / b) ) + pi
print("Theta 3_2 value is: ", round(degrees(OutTheta3_2),2 ))

OutD_2 = a*cos(theta2) - b*cos(OutTheta3_2)
print("d_2 [R1] value is: ", round(OutD_2,2))
if OutD_2 > 0:
	print("This is the real circuit.")
else:
	print("This is the non-real circuit.")