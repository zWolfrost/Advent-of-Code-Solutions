with open("input.txt", "r") as file:
	fresh_data, ingredient_ids = file.read().split("\n\n")

fresh_ranges = [id.split("-") for id in fresh_data.splitlines()]
fresh_ranges = [[int(id1), int(id2)] for id1, id2 in fresh_ranges]
ingredient_ids = [int(id) for id in ingredient_ids.splitlines()]

def is_fresh(id):
	for start, end in fresh_ranges:
		if start <= id <= end:
			return True
	return False

total_fresh_ids = sum(is_fresh(id) for id in ingredient_ids)

print("ANSWER:", total_fresh_ids)
