with open("input.txt", "r") as file:
	data = file.read().split("\n\n")

presents = [p[3:] for p in data[:-1]]
presents_size_lenient = [p.count("#") for p in presents]
presents_size_strict = [p.count("#") + p.count(".") for p in presents]
regions_size = [[int(i) for i in line.split(": ")[0].split("x")] for line in data[-1].splitlines()]
regions_list = [[int(i) for i in line.split(": ")[1].split()] for line in data[-1].splitlines()]


definitely_can_fit = 0
definitely_cannot_fit = 0
undefined_fit = 0

for region_size, region_list in zip(regions_size, regions_list):
	region_area = region_size[0] * region_size[1]
	presents_area_lenient = sum(a * b for a, b in zip(presents_size_lenient, region_list))
	presents_area_strict = sum(a * b for a, b in zip(presents_size_strict, region_list))

	if region_area < presents_area_lenient:
		definitely_cannot_fit += 1
	elif region_area >= presents_area_strict:
		definitely_can_fit += 1
	else:
		undefined_fit += 1


print(f"There are {undefined_fit} undefined regions")

print("ANSWER:", definitely_can_fit)
