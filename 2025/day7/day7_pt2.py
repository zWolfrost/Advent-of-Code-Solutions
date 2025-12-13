with open("input.txt", "r") as file:
	data = [list(line) for line in file.read().splitlines()]

for i in range(len(data)):
	for j in range(len(data[i])):
		if data[i][j] == "S": data[i][j] = 1
		elif data[i][j] == ".": data[i][j] = 0

for i in range(1, len(data)):
	for j in range(len(data[i])):
		if isinstance(data[i-1][j], int) and data[i-1][j] > 0:
			if data[i][j] == "^":
				data[i][j-1] += data[i-1][j]
				data[i][j+1] += data[i-1][j]
			else:
				data[i][j] += data[i-1][j]

timelines = sum(data[-1])

print("ANSWER:", timelines)
