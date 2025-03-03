###############################
'''
# Author: Matthew Ryan Liqua
# Date: 3/1/25
# Course: ENGR Mech Design
# Purpose: Categorizes grashof fourbar mechs
'''
###############################
print("If all the links are the same length, the mechansim is: Four Bar Mech (Class III) is: Special Case, Square (S3X)") ")
s = int(input("Input s (mm): "))
l = int(input("Input l (mm): "))
p = int(input("Input p (mm): "))
q = int(input("Input q (mm): "))

sl = s + l
pq = p + q
print("\n")

if sl < pq:
	S_ID = input("What type of link is 's': ground, input, coupler, or output?")
	print("\n")
	match S_ID:
		case "ground":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Double Crank (GCCC)")
		case "input":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Crank-Rocker (GCRR)")
		case "coupler":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Double-Rocker (GRCR)")
		case "ouput":
				print("sl < pq")
				print("Four Bar Mech (Class I) is: Grashof, Rocker-Crank (GRRC)")
		case _:
			print("You either put the [] part into the name (remove it), try again OR your input was invalid.")

elif sl > pq:
	S_ID = input("What type of link is 's': ground, input, coupler, or output?")
	print("\n")
	match S_ID:
		case "ground":
			print("sl > pq")
			print("Four Bar Mech (Class II) is: Non-Grashof, Triple-rocker (RRR1)")
		case "input":
			print("sl > pq")
			print("Four Bar Mech (Class II) is: Non-Grashof, Triple-rocker (RRR2)")
		case "coupler":
			print("sl > pq")
			print("Four Bar Mech (Class II) is: Non-Grashof, Triple-rocker (RRR3)")
		case "output":
			print("sl > pq")
			print("Four Bar Mech (Class II) is: Non-Grashof, Triple-rocker (RRR4)")
		case _:
			print("You either put the [] part into the name (remove it), try again OR your input was invalid.")

elif sl == pq:
	S_ID = input("What type of link is 's': ground, input, coupler, or output?")
	print("\n")
	match S_ID:
		case "ground":
			print("sl = pq")
			print("Four Bar Mech (Class III) is: Special Case, SC Double-Crank (SCCC)")
		case "input":
			print("sl = pq")
			print("Four Bar Mech (Class III) is: Special Case, SC Crank-Rocker (SCRR)")
		case "coupler":
			print("sl = pq")
			print("Four Bar Mech (Class III) is: Special Case, SC Doube-Rocker (SRCR)")
		case "output":
			print("sl = pq")
			print("Four Bar Mech (Class III) is: Special Case, SC Rocker-Crank (SRRC)")
		case _:
			print("You either put the [] part into the name (remove it), try again OR your input was invalid.")
else:
	print("An error has occured, try again.")