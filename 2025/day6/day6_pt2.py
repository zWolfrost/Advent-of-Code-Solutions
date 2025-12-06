with open("input.txt", "r") as file:
	data = file.read().splitlines()

data = [list(line) for line in data]

def eval_op(n1, n2, op):
	if op == "*": return n1 * n2
	elif op == "+": return n1 + n2

total_result = 0
current_result = 0
current_operation = None

for col in range(len(data[0])):
	if data[-1][col].strip():
		total_result += current_result
		current_result = None
		current_operation = data[-1][col]

	number = "".join(data[row][col] for row in range(0, len(data) - 1)).strip()

	if number:
		current_result = int(number) if current_result is None \
			else eval_op(current_result, int(number), current_operation)

total_result += current_result

print("ANSWER:", total_result)
