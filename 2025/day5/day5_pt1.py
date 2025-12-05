with open("input.txt", "r") as file:
	fresh_ranges, ingredient_ids = file.read().split("\n\n")

fresh_ranges = [id.split("-") for id in fresh_ranges.splitlines()]
ingredient_ids = ingredient_ids.splitlines()

def is_fresh(id):
	for start, end in fresh_ranges:
		if int(start) <= int(id) <= int(end):
			return True
	return False

total_fresh_ids = 0

for id in ingredient_ids:
	total_fresh_ids += is_fresh(id)

print("ANSWER:", total_fresh_ids)