from day9_utils import get_pixels_square, get_pixels_interior_perimeter

# this code takes ~40 minutes to run. TODO: find a better way

with open("input.txt", "r") as file:
	tiles = [[int(d) for d in c.split(",")] for c in file.read().splitlines()]
tiles.append(tiles[0])


perimeter = set()

for i in range(len(tiles)-1):
	perimeter.update(get_pixels_square(tiles[i], tiles[i+1]))

biggest_area = 0

for i in range(len(tiles)):
	for j in range(i+1, len(tiles)):
		interior_square = get_pixels_interior_perimeter(tiles[i], tiles[j])

		if any(c in perimeter for c in interior_square):
			continue

		area = (
			(abs(tiles[i][0] - tiles[j][0]) + 1) *
			(abs(tiles[i][1] - tiles[j][1]) + 1)
		)
		if area > biggest_area:
			biggest_area = area

print("ANSWER:", biggest_area)
