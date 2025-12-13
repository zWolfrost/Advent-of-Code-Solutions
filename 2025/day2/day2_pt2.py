with open("input.txt", "r") as file:
	data = file.read()


def is_valid_id(id: str):
	id_length = len(id)

	for seq_length in range(1, id_length):
		if id_length % seq_length == 0:
			if id == id[:seq_length] * (id_length // seq_length):
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
