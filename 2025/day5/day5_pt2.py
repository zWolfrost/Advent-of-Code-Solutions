with open("input.txt", "r") as file:
	fresh_ranges, ingredient_ids = file.read().split("\n\n")

fresh_ranges = [id.split("-") for id in fresh_ranges.splitlines()]
fresh_ranges = sorted(fresh_ranges, key=lambda r: int(r[0]))

for i in range(len(fresh_ranges)):


print(fresh_ranges)
#print("ANSWER:", len(fresh_ids_set))