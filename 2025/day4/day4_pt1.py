with open("input.txt", "r") as file:
	data = file.read()


def get_adjacent_indexes(index, width, height):
	adjacent_indexes = []

	is_not_first_col = (index % width) > 0
	is_not_last_col = (index % width) < width-1

	if index >= width:
		if is_not_first_col: adjacent_indexes.append(index - width - 1)
		adjacent_indexes.append(index - width)
		if is_not_last_col: adjacent_indexes.append(index - width + 1)

	if is_not_first_col: adjacent_indexes.append(index - 1)
	if is_not_last_col: adjacent_indexes.append(index + 1)

	if index < (height-1) * width:
		if is_not_first_col: adjacent_indexes.append(index + width - 1)
		adjacent_indexes.append(index + width)
		if is_not_last_col: adjacent_indexes.append(index + width + 1)

	return adjacent_indexes


data_width = len(data.splitlines()[0])
data_height = len(data.splitlines())
data_flat = list(data.replace("\n", ""))

accessable_rolls = 0

for i in range(len(data_flat)):
	if data_flat[i] == "@":
		adjacent_indexes = get_adjacent_indexes(i, data_width, data_height)
		adjacent_rolls = sum(data_flat[adj] == "@" for adj in adjacent_indexes)

		accessable_rolls += (adjacent_rolls < 4)

print("ANSWER:", accessable_rolls)
