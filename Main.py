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
	Case 1 (Four Bar): Theta 3 and Theta 4 unknown
	Case 2 (Crank Slider): d and Theta 3 unknown
	Case 3 (Slider Crank): Theta 2 and Theta 3 unknown
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
	case _:
		print("That is an invalid input, try again.")
