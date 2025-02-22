###################
'''
# Author: Matthew Ryan Liqua
# Created Date: 2/22/25
# Last Edited Date: 2/22/25
# Course: ENGR Mechanism Design
# Purpose: Positional, Velocity, and Accleration Of
		   Four bar mechanism
# test values: a = 100mm, b = 40mm, c = 120mm, d = 80
				theta1 = 0, theta2 = 60
'''
####################################################
# Derivation was done on another sheet of paper

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

L1 = int(input("Input L1 (mm): "))
L2 = int(input("Input L2 (mm): "))
L3 = int(input("Input L3 (mm): "))
L4 = int(input("Input L4 (mm): "))  

theta1 = radians(int(input("Input theta 1 (degree): ")))
theta2 = radians(int(input("Input theta 2 (degree): ")))
#theta3 = radians(int(input("Input theta 3 (degree): ")))
#theta4 = radians(int(input("Input theta 4 (degree): "))) 

K1 = L4 / L1
K2 = L4 / L3
K3 = ( (L1**2) - (L2**2) + (L3**2) + (L4**2) ) / (2 * L1 * L3)
#print("These are the values K1, K2, and K3:", K1, K2, K3)


A = cos(theta2) - K1 - (K2*cos(theta2)) + K3
B = -2*sin(theta2)
C = K1 - (K2 + 1)*cos(theta2) + K3
#print("These are the values A,B,C: ", A, B, C)

print("\n")
####################################################
# Calculating Theta 4

TempVal_1 = - B + sqrt( (B**2) -4*A*C)
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*A)
TempVal_3 = 2*atan(TempVal_2)
TempVal_3 = round(degrees(TempVal_3), 2)
print("First Theta 4 Value:", TempVal_3)

TempVal_1 = - B - sqrt( (B**2) -4*A*C)
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*A)
TempVal_3 = 2*atan(TempVal_2)
TempVal_3 = round(degrees(TempVal_3), 2)
print("Second Theta 4 Value:", TempVal_3)
print("\n")

####################################################
# Calculating Theta 3

K4 = L4 / L2
K5 = ( (L3**2) - (L4**2) - (L1**2) - (L2**2) ) / (2*L1*L2)
#print("K1, K4, k5:", K1, K4, K5)

D = cos(theta2) - K1 + K4*cos(theta2) + K5
E = -2*sin(theta2)
F = K1 + (K4 - 1)*cos(theta2) + K5
#print("D,E,F: ", D,E,F)

TempVal_1 = - F + sqrt( (E**2) -4*D*F)
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*D)
TempVal_3 = 2*atan(TempVal_2)
TempVal_3 = round(degrees(TempVal_3), 2)
print("First Theta 3 Value: ", TempVal_3)

TempVal_1 = - F - sqrt( (E**2) -4*D*F)
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*D)
TempVal_3 = 2*atan(TempVal_2)
TempVal_3 = round(degrees(TempVal_3), 2)
print("Second Theta 3 Value: ", TempVal_3)

# Expand with velocity and accleration