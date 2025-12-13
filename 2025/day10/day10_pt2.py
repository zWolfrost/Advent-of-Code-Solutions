with open("input.txt", "r") as file:
	machines = [m.split(" ") for m in file.read().splitlines()]

lights_lst = [[False if c == "." else True for c in m[0][1:-1]] for m in machines]
buttons_lst = [[[int(n) for n in c[1:-1].split(",")] for c in m[1:-1]] for m in machines]
joltage_lst = [[int(n) for n in m[-1][1:-1].split(",")] for m in machines]


from pulp import LpProblem, LpVariable, LpMinimize, LpInteger, lpSum, PULP_CBC_CMD

def min_button_presses(target, buttons):
	num_buttons = len(buttons)
	num_counters = len(target)

	prob = LpProblem("MinButtonPresses", LpMinimize)

	x = [LpVariable(f"x{i}", lowBound=0, cat=LpInteger) for i in range(num_buttons)]

	prob += lpSum(x)

	for j in range(num_counters):
		prob += lpSum(buttons[i][j] * x[i] for i in range(num_buttons)) == target[j]

	prob.solve(PULP_CBC_CMD(msg=False))

	if prob.status != 1:
		return None

	return sum(int(x[i].varValue) for i in range(num_buttons))


presses_total = 0

for i, (joltage, buttons) in enumerate(zip(joltage_lst, buttons_lst)):
	vectors = [[0 for _ in range(len(joltage))] for _ in range(len(buttons))]

	for i, btn in enumerate(buttons):
		for n in btn:
			vectors[i][n] = 1

	presses_total += min_button_presses(joltage, vectors)

print("ANSWER:", presses_total)
