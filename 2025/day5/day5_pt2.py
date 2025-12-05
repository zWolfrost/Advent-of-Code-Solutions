with open("input.txt", "r") as file:
	fresh_data = file.read().split("\n\n")[0]

fresh_ranges = [id.split("-") for id in fresh_data.splitlines()]
fresh_ranges = [[int(id1), int(id2)] for id1, id2 in fresh_ranges]

def optimize_ranges(ranges: list[int, int]):
	sorted_ranges = sorted(ranges, key=lambda r: r[0])
	while True:
		has_optimized = False
		i = 0
		while i < len(sorted_ranges) - 1:
			if sorted_ranges[i][1] >= sorted_ranges[i+1][0]:
				if sorted_ranges[i][1] <= sorted_ranges[i+1][1]:
					sorted_ranges[i][1] = sorted_ranges[i+1][1]
				sorted_ranges.pop(i+1)
				has_optimized = True
			i += 1
		if not has_optimized:
			break
	return sorted_ranges

optimized_ranges = optimize_ranges(fresh_ranges)

total_fresh_ids = sum(end - start + 1 for start, end in optimized_ranges)

print("ANSWER:", total_fresh_ids)
