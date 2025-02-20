###############################

# Author: Matthew Ryan Liqua
# Date:2/19/25
# Course: ENGR Mech Design

###############################

from math import sin, cos, tan, acos, asin, atan, pi, degrees, radians

L1 = int(input("Input L1 (mm): "))
L2 = int(input("Input L2 (mm): "))
L3 = int(input("Input L1 (mm): "))
L4 = int(input("Input L2 (mm): "))  

theta1 = radians(int(input("Input theta 1 (degree): ")))
theta2 = radians(int(input("Input theta 2 (degree): ")))
theta3 = radians(int(input("Input theta 3 (degree): ")))
theta4 = radians(int(input("Input theta 4 (degree): "))) 

# asin is a multi valued function, hence OutTheta3_2
OutTheta3_1 = asin( ((L1 * sin(theta2) - L3) / L2) )
print("The first theta 3 value is: ", round(degrees(OutTheta3_1),2))

OutTheta3_2 = asin( - ((L1 * sin(theta2) - L3) / L2) ) + pi
print("The second theta 3 value is: ", round(degrees(OutTheta3_2),2 ))

OutD_1 = L1*cos(theta2) - L2*cos(OutTheta3_1)
print("The first L4 value is: ", round(OutD_1,2))

OutD_2 = L1*cos(theta2) - L2*cos(OutTheta3_2)
print("The second L4 value is: ", round(OutD_2,2))
