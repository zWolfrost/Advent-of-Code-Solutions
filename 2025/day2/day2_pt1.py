with open("input.txt", "r") as file:
	data = file.read()


def is_valid_id(id: str):
	id_length = len(id)

	if id_length % 2 == 0:
		if id == id[:id_length//2] * 2:
			return False

	return True


sum_invalid = 0

for bulk in data.split(","):
	start, end = bulk.split("-")
	start = int(start)
	end = int(end)

	for id in range(start, end+1):
		if not is_valid_id(str(id)):
			sum_invalid += id

print("ANSWER:", sum_invalid)
