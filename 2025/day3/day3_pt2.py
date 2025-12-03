with open("input.txt", "r") as file:
	data = file.read().splitlines()

BATTERIES_TO_CHOOSE = 12 # set to 2 for pt.1

total_joltage = 0

for bank in data:
	max_joltages = ""

	for n in range(BATTERIES_TO_CHOOSE-1, -1, -1):
		cur_max = max(bank[:-n]) if n != 0 else max(bank)
		max_joltages += str(cur_max)

		bank = bank.split(cur_max, 1)[1]

	total_joltage += int(max_joltages)

print("ANSWER:", total_joltage)
