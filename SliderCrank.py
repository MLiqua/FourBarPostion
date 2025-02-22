##########################################################
'''
# Author: Matthew Ryan Liqua
# Date Created: 2/19/25
# Date Last Edited: 2/22/25
# Course: ENGR Mechanism Design
# Purpose: Calcualte Positional, Velocity, And Accleration
		   For Slider Crank Mechanism
'''
##########################################################

# Derivation was done on another page
# The goal here is to solve for theta 2 and theta 3

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

L1 = int(input("Input L1 (mm): "))
L2 = int(input("Input L2 (mm): "))
L3 = int(input("Input L3 (mm): "))
L4 = int(input("Input L4 (mm): "))  

theta1 = radians(int(input("Input theta 1 (degree): ")))
# theta2 = radians(int(input("Input theta 2 (degree): ")))
# theta3 = radians(int(input("Input theta 3 (degree): ")))
theta4 = radians(int(input("Input theta 4 (degree): "))) 
print("\n")

K1 = (L1 ** 2) - (L2 ** 2) + (L3 ** 2) + (L4 ** 2)
K2 = -2 * L1 * L3
K3 = -2 * L1 * L4
#print("These are the values K1, K2, and K3:", K1, K2, K3)

A = K1 - K3
B = 2*K2
C = K1 + K3
#print("These are the values A,B,C: ", A, B, C)

##########################################################
# First Angle Solving
TempVal_1 = -B + sqrt( (B ** 2) - 4 * A * C )
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*A)

Theta2_1 = round(degrees(2*atan(TempVal_2)),2)
print("First theta 2 value: ", Theta2_1)

TempVal_1 = radians(Theta2_1)
TempVal_2 = (L1 * sin(TempVal_1) - L3) / L2
TempVal_3 = round(degrees(asin(TempVal_2)), 2)
print("First Theta 3 value from First Theta 2: ", TempVal_3)

# Asin is a multi-value function, thus add pi
TempVal_1 = radians(Theta2_1)
TempVal_2 = -(L1 * sin(TempVal_1) - L3) / L2
TempVal_3 = round(degrees( asin(TempVal_2) + pi), 2)
print("Second Theta 3 value from First Theta 2: ", TempVal_3)
print("\n")


# Further expansion to include velocity and accleration

##########################################################
# Second Angle Solving
TempVal_1 = -B - sqrt( (B ** 2) - 4 * A * C )
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*A)

Theta2_2 = round(degrees(2*atan(TempVal_2)),2)
print("Second theta2 value: ", Theta2_2)

TempVal_1 = radians(Theta2_2)
TempVal_2 = (L1 * sin(TempVal_1) - L3) / L2
TempVal_3 = round(degrees(asin(TempVal_2)), 2)
print("First Theta 3 value from Second Theta 2: ", TempVal_3)

TempVal_1 = radians(Theta2_2)
TempVal_2 = -(L1 * sin(TempVal_1) - L3) / L2
TempVal_3 = round(degrees( asin(TempVal_2) + pi), 2)
print("Second Theta 3 value from Second Theta 2: ", TempVal_3)


# Further expansion to include velocity and accleration