###################

# Author: Matthew Ryan Liqua
# Date: 2/19/25
# Course: ENGR Mechanism Design

###################

# The goal here is to solve for theta2 and theta3

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

L1 = int(input("Input L1 (mm): "))
L2 = int(input("Input L2 (mm): "))
L3 = int(input("Input L1 (mm): "))
L4 = int(input("Input L2 (mm): "))  

theta1 = radians(int(input("Input theta 1 (degree): ")))
# theta2 = radians(int(input("Input theta 2 (degree): ")))
# theta3 = radians(int(input("Input theta 3 (degree): ")))
theta4 = radians(int(input("Input theta 4 (degree): "))) 
print("\n")

# Derivation was done on another page
K1 = (L1 ** 2) - (L2 ** 2) + (L3 ** 2) + (L4 ** 2)
K2 = -2 * L1 * L3
K3 = -2 * L1 * L4
#print("These are the values K1, K2, and K3:", K1, K2, K3)

A = K1 - K3
B = 2*K2
C = K1 + K3
#print("These are the values A,B,C: ", A, B, C)

TempVal_1 = -B + sqrt( (B ** 2) - 4 * A * C )
# .real only stores real part of complex data value
TempVal_1 = TempVal_1.real
TempVal_2 = TempVal_1 / (2*A)

Theta2_1 = round(degrees(2*atan(TempVal_2)),2)
print("This is the first theta2 value: ", Theta2_1)

