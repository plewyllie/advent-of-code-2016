inputd = "L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4"

moves = inputd.replace(" ", "").split(",")

facing = "N"
vertical = 0
horizontal = 0

for move in moves:
	print("move " + move)
	direc = move[0]
	nb = int(move[1:])
	if facing == "N":
		if direc == "R":
			horizontal += nb
			facing = "E"
		if direc == "L":
			horizontal -= nb
			facing = "W"
	elif facing == "W":
		if direc == "R":
			vertical += nb
			facing = "N"
		if direc == "L":
			vertical -= nb
			facing = "S"
	elif facing == "E":
		if direc == "R":
			vertical -= nb
			facing = "S"
		if direc == "L":
			vertical += nb
			facing = "N"
	elif facing == "S":
		if direc == "R":
			horizontal -= nb
			facing = "W"
		if direc == "L":
			horizontal += nb
			facing = "E"

print("Vertical " + str(vertical) + " and horizontal " + str(horizontal))
print("Total blocks away is " + str(vertical + horizontal))




