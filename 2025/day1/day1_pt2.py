with open("input.txt", "r") as file:
	instructions = file.read().splitlines()

number = 50
zeroes = 0
for instruction in instructions:
	direction = -1 if instruction[0] == "L" else 1
	steps = int(instruction[1:])

	for _ in range(steps):
		number += direction
		number = number % 100

		if number == 0:
			zeroes += 1

print("ANSWER:", zeroes)
