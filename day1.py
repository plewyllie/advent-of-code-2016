inputd = "R5, L5, R5, R3"

moves = inputd.replace(" ", "").split(",")

facing = "N"
vertical = 0
horizontal = 0

for move in moves:
	print("move " + move)
	if facing == "N":
		if move[0] == "R":
			horizontal += int(move[1])
			facing = "E"
		if move[0] == "L":
			horizontal -= int(move[1])
			facing = "W"
	elif facing == "W":
		if move[0] == "R":
			vertical += int(move[1])
			facing = "N"
		if move[0] == "L":
			vertical -= int(move[1])
			facing = "S"
	elif facing == "E":
		if move[0] == "R":
			vertical -= int(move[1])
			facing = "S"
		if move[0] == "L":
			vertical += int(move[1])
			facing = "N"
	elif facing == "S":
		if move[0] == "R":
			horizontal -= int(move[1])
			facing = "W"
		if move[0] == "L":
			horizontal += int(move[1])
			facing = "E"

print("Vertical " + str(vertical) + " and horizontal " + str(horizontal))



