###############################
'''
# Author: Matthew Ryan Liqua
# Date:2/19/25
# Course: ENGR Mech Design
# Purpose: Calcuates postion, velocity, and accleration
			of crank slider mechanism
'''
####################################################

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

L1 = int(input("Input L1 (mm): "))
L2 = int(input("Input L2 (mm): "))
L3 = int(input("Input L3 (mm): "))
# L4 = int(input("Input L4 (mm): "))  

theta1 = radians(int(input("Input theta 1 (degree): ")))
theta2 = radians(int(input("Input theta 2 (degree): ")))
#theta3 = radians(int(input("Input theta 3 (degree): ")))
theta4 = radians(int(input("Input theta 4 (degree): "))) 
print("\n")

####################################################
# First theta 3 value

OutTheta3_1 = asin( ((L1 * sin(theta2) - L3) / L2) )
print("First theta 3 value is: ", round(degrees(OutTheta3_1),2))

OutD_1 = L1*cos(theta2) - L2*cos(OutTheta3_1)
print("First L4 ('d') value in mm:", round(OutD_1,2))
print("\n")

####################################################
# Second theta 3 value
# asin is a multi valued function, hence OutTheta3_2
OutTheta3_2 = asin( - ((L1 * sin(theta2) - L3) / L2) ) + pi
print("Second theta 3 value is: ", round(degrees(OutTheta3_2),2 ))

OutD_2 = L1*cos(theta2) - L2*cos(OutTheta3_2)
print("Second L4 ('d') value in mm: ", round(OutD_2,2))
