###############################
'''
# Author: Matthew Ryan Liqua
# Date: 3/1/25
# Course: ENGR Mech Design
# Purpose: Categorizes grashof fourbar mechs
'''
###############################

s = int(input("Input s (mm): "))
l = int(input("Input l (mm): "))
p = int(input("Input p (mm): "))
q = int(input("Input q (mm): "))
sl = s + l
pq = p + q
print("\n")

if sl < pq:
	user_input = input("Which is shortest link (frame [L1], input [L2], or coupler [L3])?: ")
	print("\n")
	match user_input:
		case "frame":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Double Crank")
		case "input":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Crank-Rocker")
		case "coupler":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Double-Rocker")
		case _:
			print("You either put the [] part into the name (remove it), try again OR your input was invalid.")
elif sl > pq:
	print("sl > pq")
	print("Four Bar Mech (Class II) is: Non-Grashof, Triple-rocker")
elif sl == pq:
	print("sl = pq")
	print("Four Bar Mech (Class III) is: Change Point")
else:
	print("An error has occured, try again.")