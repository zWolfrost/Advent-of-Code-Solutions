with open("input.txt", "r") as file:
	tiles = [[int(d) for d in c.split(",")] for c in file.read().splitlines()]

biggest_area = 0

for i in range(len(tiles)):
	for j in range(i+1, len(tiles)):
		area = (
			(abs(tiles[i][0] - tiles[j][0]) + 1) *
			(abs(tiles[i][1] - tiles[j][1]) + 1)
		)
		if area > biggest_area:
			biggest_area = area

print("ANSWER:", biggest_area)
