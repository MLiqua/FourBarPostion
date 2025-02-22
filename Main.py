############################
'''
# Author: Matthew R. Liqua
# Course: ENGR Mechanism
# Date Created: 2/20/25
# Last Edited: 2/22/25
# Purpose: Main File. Used To Run File For Given Inputs
		   For Four Bar Mechanisms
'''
############################

print("Please write the name of the file that you want executed: ")
UserInput = input()


# Takes UserInput and reads the file
with open(UserInput) as file:
	code = file.read()
	exec(code)