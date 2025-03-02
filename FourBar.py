###################
'''
# Author: Matthew Ryan Liqua
# Created Date: 2/22/25
# Last Edited Date: 3/1/25
# Course: ENGR Mechanism Design
# Purpose: Positional, Velocity, and Accleration Of
		   Four bar mechanism
'''
####################################################
# Derivation done on FourBarDer.txt

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians
from cmath import sqrt

print("\n")
print("This calculation assumes ground is d [R1]")
print("Ensure that all units for length are the same.")
a = float(input("Input a [R2] length: "))
b = float(input("Input b [R3] length: "))
c = float(input("Input c [R4] length: "))
d = float(input("Input d [R1] length: "))  
theta2 = radians(float(input("Input theta 2 (degree): ")))
#print("This is theta2: ", theta2)

#omega2 = int(input("Input omega 2 (rad/s): "))

K1 = d / a
K2 = d / c
K3 = ( (a**2) - (b**2) + (c**2) + (d**2) ) / (2 * a * c)
#print("These are the values K1, K2, and K3:", K1, K2, K3)


A = cos(theta2) - K1 - (K2*cos(theta2)) + K3
B = -2*sin(theta2)
C = K1 - (K2 + 1)*cos(theta2) + K3
#print("These are the values A,B,C: ", A, B, C)

print("\n")
####################################################
# Calculating Theta 4

TopPartQuad = - B + sqrt( (B**2) -4*A*C)
TopPartQuad = TopPartQuad.real
InsideATan = TopPartQuad / (2*A)
RadATanVal = atan(InsideATan)
RadATanVal = 2*RadATanVal
RadTheta4_1 = RadATanVal # Value stored for vector applicaiton later
Theta4_1 = round(degrees(RadATanVal), 2)
print("Theta 4_1 Value:", Theta4_1)

TopPartQuad = - B - sqrt( (B**2) -4*A*C)
TopPartQuad = TopPartQuad.real
InsideATan = TopPartQuad / (2*A)
RadATanVal = atan(InsideATan)
RadATanVal = 2*RadATanVal
RadTheta4_2 = RadATanVal
Theta4_2 = round(degrees(RadATanVal), 2)
print("Theta 4_2 Value:", Theta4_2)
print("\n")

####################################################
# Calculating Theta 3

K4 = d / b
K5 = ( (c**2) - (d**2) - (a**2) - (b**2) ) / (2*a*b)
#print("K1, K4, k5:", K1, K4, K5)

capD = cos(theta2) - K1 + K4*cos(theta2) + K5
capE = -2*sin(theta2)
capF = K1 + (K4 - 1)*cos(theta2) + K5
#print("D,E,F: ", D,E,F)

TopPartQuad = - capE + sqrt( (capE**2) -4*capD*capF)
TopPartQuad = TopPartQuad.real
InsideATan = TopPartQuad / (2*capD)
RadATanVal = atan(InsideATan)
RadATanVal = 2*RadATanVal
RadTheta3_1 = RadATanVal
Theta3_1 = round(degrees(RadATanVal), 2)
print("Theta 3_1 Value:", Theta3_1)

TopPartQuad = - capE - sqrt( (capE**2) -4*capD*capF)
TopPartQuad = TopPartQuad.real
InsideATan = TopPartQuad / (2*capD)
RadATanVal = atan(InsideATan)
RadATanVal = 2*RadATanVal
RadTheta3_2 = RadATanVal
Theta3_2 = round(degrees(RadATanVal), 2)
print("Theta 3_2 Value: ", Theta3_2)
print("\n")


####################################################
#Graphing vector loop to determine open vs crossed config

import numpy as np
import matplotlib.pyplot as plt

# x = rcos(theta)
# y = rsin(theta)
R1_x = d * cos(0) 
R1_y = d * sin(0)

R2_x = a * cos(theta2)
R2_y = a * sin(theta2)


R3_x_1 = b * cos(RadTheta3_1)
R3_y_1 = b * sin(RadTheta3_1)
R3_x_2 = b * cos(RadTheta3_2)
R3_y_2 = b * sin(RadTheta3_2)


R4_x_1 = c * cos(RadTheta4_1)
R4_y_1 = c * sin(RadTheta4_1)
R4_x_2 = c * cos(RadTheta4_2)
R4_y_2 = c * sin(RadTheta4_2)

# BE VERY MINDFUL OF VECOTR ARROW DIRECTION
ax = plt.axes()
ax.arrow(0,0, R1_x, R1_y, head_width = .25, head_length = .25, color = 'blue', label = 'd [R1]') # R1
ax.arrow(0,0, R2_x, R2_y, head_width = .25, head_length = .25, color = 'red', label = 'a [R2]') # R2
ax.arrow(R2_x, R2_y, R3_x_1, R3_y_1, head_width = .25, head_length = .25, color = 'orange', label = 'b [R3]') # R3
ax.arrow(R1_x, R1_y, R4_x_1, R4_y_1, head_width = .25, head_length = .25, color = 'green', label = 'c [R4]') #R4

plt.xlim(0,150)
plt.ylim(0,150)
plt.legend()
plt.title('First Four-Bar, Using Theta3_1 & Theta4_1')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid()
plt.show()

# Second Plot, Opens After You Close First
ax_2 = plt.axes()
ax_2.arrow(0,0, R1_x, R1_y, head_width = .25, head_length = .25, color = 'blue', label = 'd [R1]') # R1
ax_2.arrow(0,0, R2_x, R2_y, head_width = .25, head_length = .25, color = 'red', label = 'a [R2]') # R2
ax_2.arrow(R2_x, R2_y, R3_x_2, R3_y_2, head_width = .25, head_length = .25, color = 'orange', label = 'b [R3]') # R3
ax_2.arrow(R1_x, R1_y, R4_x_2, R4_y_2, head_width = .25, head_length = .25, color = 'green', label = 'c [R4]') #R4

plt.xlim(0,150)
plt.ylim(0,150)
plt.legend()
plt.title('Second Four-Bar, Using Theta3_2 & Theta4_2')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid()
plt.show()

'''

####################################################
# Calculating W4

TempVal_1 = L1 * omega2 * sin(theta2 - Theta3_1)
TempVal_2 = L3 * sin(Theta4_1 - Theta3_1)
Omega4_1 = TempVal_1 / TempVal_2
print("The first omega 4 value: ", Omega4_1)

####################################################
# Calculating W3

TempVal_1 = L1 * omega2 * sin(Theta4_2 - theta2)
TempVal_2 = L2 * sin(Theta3_1 - Theta4_1)
Omega3 = TempVal_1 / TempVal_2
print("This is the Omega 3 value: ", Omega3)

# Expand with velocity and accleration

####################################################
# Working to graph the data

'''
