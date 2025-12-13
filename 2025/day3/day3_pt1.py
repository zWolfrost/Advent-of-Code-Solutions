with open("input.txt", "r") as file:
	data = file.read().splitlines()

total_joltage = 0

for bank in data:
	max1 = max(bank[:-1])
	max2 = max(bank.split(max1, 1)[1])
	total_joltage += int(str(max1) + str(max2))

print("ANSWER:", total_joltage)
