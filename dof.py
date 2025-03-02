###################
'''
# Author: Matthew Ryan Liqua
# Created Date: 3/2/25
# Last Edited Date: 3/2/25
# Course: ENGR Mechanism Design
# Purpose: DOF calculator
'''
####################################################

# Calculations done using Kutzbach eq

Links = int(input("Input number of links: "))
FullJ = int(input("Input number of full joints: "))
HalfJ = int(input("Input number of half joints: "))

DOF = (3*(Links - 1)) - (2*FullJ) - HalfJ
print("The Degrees Of Freedom (M) is: ", DOF)
