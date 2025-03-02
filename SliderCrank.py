##########################################################
'''
# Author: Matthew Ryan Liqua
# Date Created: 2/19/25
# Date Last Edited: 3/2/25
# Course: ENGR Mechanism Design
# Purpose: Calcualte Positional, Velocity, And Accleration
		   For Slider Crank Mechanism
'''
##########################################################
# Derivation done on SliderCrank_Der

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

print("\n")
print("This calculation assumes ground is d [R1] & Theta4 = 90")
print("Ensure that all units for length are the same.")
a = float(input("Input a [R2] length: "))
b = float(input("Input b [R3] length: "))
c = float(input("Input c [R4] length: "))
d = float(input("Input d [R1] length: "))  
print("\n")

K1 = (a ** 2) - (b ** 2) + (c ** 2) + (d ** 2)
K2 = -2*a*c
K3 = -2*a*d
# print("These are the values K1, K2, and K3:", K1, K2, K3)

A = K1 - K3
B = 2*K2
C = K1 + K3
# print("These are the values A,B,C: ", A, B, C)

##########################################################
# First Angle Solving
# B/C Theta 2 is not defined, it can be anywhere in space, hence you see branching behvaior (Theta3)

TopPartQuad = - B + sqrt( (B**2) -4*A*C)
TopPartQuad = TopPartQuad.real
InsideATan = TopPartQuad / (2*A)
RadATanVal = atan(InsideATan)
RadATanVal = 2*RadATanVal
RadTheta2_1 = RadATanVal # Value stored for vector applicaiton later
Theta2_1 = round(degrees(RadTheta2_1), 2)
print("NOTE: First '_' = Theta2 value used for calculation.")
print("NOTE: Second '_' = Theta3 value calculated.")
print("\n")
print("Theta 2_1 Value:", Theta2_1)

TopFraction =  (a*sin(RadTheta2_1) - c) / b
RadTheta3_1_1 = asin(TopFraction)
Theta3_1_1 = round(degrees(RadTheta3_1_1), 2)
print("Theta 3_1_1 value from Theta2_1: ", Theta3_1_1)

# Asin is a multi-value function, thus add pi (radian value)
TopFraction =  -(a*sin(RadTheta2_1) - c) / b
RadTheta3_1_2 = asin(TopFraction) + pi
Theta3_1_2 = round(degrees(RadTheta3_1_2), 2)
print("Theta 3_1_2 value from Theta2_1: ", Theta3_1_2)
print("\n")

##########################################################
# Second Angle Solving
TopPartQuad = - B - sqrt( (B**2) -4*A*C)
TopPartQuad = TopPartQuad.real
InsideATan = TopPartQuad / (2*A)
RadATanVal = atan(InsideATan)
RadATanVal = 2*RadATanVal
RadTheta2_2 = RadATanVal # Value stored for vector applicaiton later
Theta2_2 = round(degrees(RadTheta2_2), 2)
print("Theta 2_2 Value: ", Theta2_2)

TopFraction =  (a*sin(RadTheta2_2) - c) / b
RadTheta3_2_1 = asin(TopFraction)
Theta3_2_1 = round(degrees(RadTheta3_2_1), 2)
print("Theta 3_2_1 value from Theta2_2: ", Theta3_2_1)

TopFraction =  -(a*sin(RadTheta2_2) - c) / b
RadTheta3_2_2 = asin(TopFraction) + pi
Theta3_2_2 = round(degrees(RadTheta3_2_2), 2)
print("Theta 3_2_2 value from Theta2_2: ", Theta3_2_2)
print("\n")

# Further expand graphical capabilities to show real and non-real circuits
# Further expansion to include velocity and accleration