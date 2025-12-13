with open("input.txt", "r") as file:
	data = [list(line) for line in file.read().replace("S", "|").splitlines()]

splitted_beams = 0

for i in range(1, len(data)):
	for j in range(len(data[i])):
		if data[i][j] == "." and data[i-1][j] == "|":
			data[i][j] = "|"
		elif data[i][j] == "^" and data[i-1][j] == "|":
			data[i][j-1] = data[i][j+1] = "|"
			splitted_beams += 1

print("ANSWER:", splitted_beams)
