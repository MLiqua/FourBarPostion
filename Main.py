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

print("""
	Please select from one of the cases below:
	Case 1: Theta 3 and Theta 4 unknown (Four Bar)
	Case 2: d and Theta 3 unknown (Crank Slider)
	Case 3: Theta 2 and Theta 3 unknown (Slider Crank)
	Case 4: ID Grashof Four Bar Mech
	Case 5: DOF (M) Calculator
""")
print("Type numeric part of case that you want: ") 
UserInput = input()

match UserInput:
	case "1":
			with open("FourBar.py") as file:
				code = file.read()
				exec(code)

	case "2":
			with open("CrankSlider.py") as file:
				code = file.read()
				exec(code)
	case "3":
			with open("SliderCrank.py") as file:
				code = file.read()
				exec(code)
	case "4":
		with open("GrashofFour.py") as file:
				code = file.read()
				exec(code)
	case "5":
		with open("dof.py") as file:
				code = file.read()
				exec(code)
	case _:
		print("That is an invalid input, try again.")
