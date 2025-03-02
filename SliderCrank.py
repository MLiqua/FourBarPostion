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

###################################################
#Graphing The Vector Loops
import numpy as np
import matplotlib.pyplot as plt

R1_x = d * cos(0) 
R1_y = d * sin(0)
R4_x_1 = c * cos(1.5707) # Goes to 0
R4_y_1 = c * sin(1.5707)

# Plot 1 Values: Theta2_1 & Theta3_1_1
Theta2_1_R2_x = a * cos(RadTheta2_1)
Theta2_1_R2_y = a * sin(RadTheta2_1)
Theta3_1_1_R3_x = b * cos(RadTheta3_1_1)
Theta3_1_1_R3_y = b * sin(RadTheta3_1_1)

# Plot 2 Values: Theta2_1 & Theta3_1_2
Theta3_1_2_R3_x = b * cos(RadTheta3_1_2)
Theta3_1_2_R3_y = b * sin(RadTheta3_1_2)

# Plot 3 Values: Theta2_2 & Theta3_2_1
Theta2_2_R2_x = b * cos(RadTheta2_2)
Theta2_2_R2_y = b * sin(RadTheta2_2)
Theta3_2_1_R3_x = b * cos(RadTheta3_2_1)
Theta3_2_1_R3_y = b * sin(RadTheta3_2_1)

# Plot 4 Values: Theta2_2 & Theta3_2_2
Theta3_2_2_R3_x = b * cos(RadTheta3_2_2)
Theta3_2_2_R3_y = b * sin(RadTheta3_2_2)

# BE VERY MINDFUL OF VECOTR ARROW DIRECTION
ax = plt.axes()
ax.arrow(0,0, R1_x, R1_y, head_width = 1, head_length = 1, color = 'blue', label = 'd [R1]') # R1
ax.arrow(0,0, Theta2_1_R2_x, Theta2_1_R2_y, head_width = 1, head_length = .1, color = 'red', label = 'a [R2]') # R2
ax.arrow( (R4_x_1+d) , R4_y_1, Theta3_1_1_R3_x, Theta3_1_1_R3_y, head_width = 1, head_length = 1, color = 'orange', label = 'b [R3]') # R3
ax.arrow(R1_x, R1_y, R4_x_1, R4_y_1, head_width = 1, head_length = 1, color = 'green', label = 'c [R4]') #R4

plt.xlim(0,150)
plt.ylim(0,150)
plt.legend()
plt.title('Slider-Crank(Using: Theta2_1 & Theta3_1_1')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid()
plt.show()

# Second Plot, Opens After You Close First
ax_2 = plt.axes()
ax_2.arrow(0,0, R1_x, R1_y, head_width = 1, head_length = 1, color = 'blue', label = 'd [R1]') # R1
ax_2.arrow(0,0, Theta2_1_R2_x, Theta2_1_R2_y, head_width = 1, head_length = .1, color = 'red', label = 'a [R2]') # R2
ax_2.arrow( (R4_x_1+d) , R4_y_1, Theta3_1_2_R3_x, Theta3_1_2_R3_y, head_width = 1, head_length = 1, color = 'orange', label = 'b [R3]') # R3
ax_2.arrow(R1_x, R1_y, R4_x_1, R4_y_1, head_width = 1, head_length = 1, color = 'green', label = 'c [R4]') #R4

plt.xlim(0,150)
plt.ylim(0,150)
plt.legend()
plt.title('Slider-Crank(Using: Theta2_1 & Theta3_1_2)')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid()
plt.show()

# Third Plot, Opens After You Close First
ax_3 = plt.axes()
ax_3.arrow(0,0, R1_x, R1_y, head_width = 1, head_length = 1, color = 'blue', label = 'd [R1]') # R1
ax_3.arrow(0,0, Theta2_2_R2_x, Theta2_2_R2_y, head_width = 1, head_length = .1, color = 'red', label = 'a [R2]') # R2
ax_3.arrow( (R4_x_1+d) , R4_y_1, Theta3_2_1_R3_x, Theta3_2_1_R3_y, head_width = 1, head_length = 1, color = 'orange', label = 'b [R3]') # R3
ax_3.arrow(R1_x, R1_y, R4_x_1, R4_y_1, head_width = 1, head_length = 1, color = 'green', label = 'c [R4]') #R4

plt.xlim(0,150)
plt.ylim(0,150)
plt.legend()
plt.title('Slider-Crank(Using: Theta2_2 & Theta3_2_1')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid()
plt.show()

# Fourth Plot, Opens After You Close First
# May have issues, not sure
ax_4 = plt.axes()
ax_4.arrow(0,0, R1_x, R1_y, head_width = 1, head_length = 1, color = 'blue', label = 'd [R1]')
ax_4.arrow(0,0, Theta2_2_R2_x, Theta2_2_R2_y, head_width = 1, head_length = .1, color = 'red', label = 'a [R2]')
ax_4.arrow((R4_x_1+d) , R4_y_1, Theta3_2_2_R3_x, Theta3_2_2_R3_y, head_width = 1, head_length = 1, color = 'orange', label = 'b [R3]')
ax_4.arrow(R1_x, R1_y, R4_x_1, R4_y_1, head_width = 1, head_length = 1, color = 'green', label = 'c [R4]')

plt.xlim(0,150)
plt.ylim(0,150)
plt.legend()
plt.title('Slider-Crank(Using: Theta2_2 & Theta3_2_2')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.axis('equal')
plt.grid()
plt.show()


# Further expand graphical capabilities to show real and non-real circuits
# Further expansion to include velocity and accleration