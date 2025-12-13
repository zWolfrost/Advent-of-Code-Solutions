with open("input.txt", "r") as file:
	data = file.read().splitlines()

data = [line.split() for line in data]

def eval_op(n1, n2, op):
	if op == "*": return n1 * n2
	elif op == "+": return n1 + n2

total_result = 0

for col in range(len(data[0])):
	op = data[-1][col]
	result = int(data[0][col])
	for row in range(1, len(data) - 1):
		result = eval_op(result, int(data[row][col]), op)
	total_result += result

print("ANSWER:", total_result)
