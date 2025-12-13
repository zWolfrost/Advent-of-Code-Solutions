from day8_utils import rank_distance, UnionFind

with open("input.txt", "r") as file:
	boxes = [[int(c) for c in coords.split(",")] for coords in file.read().splitlines()]


boxes_pairs = []

for i in range(len(boxes)):
	for j in range(i+1, len(boxes)):
		dist = rank_distance(boxes[i], boxes[j])
		boxes_pairs.append([i, j, dist])

boxes_pairs = sorted(boxes_pairs, key=lambda d: d[2])

for i in range(len(boxes_pairs)):
	boxes_pairs[i].pop(2)


uf = UnionFind(len(boxes))
last_connection = []
for i in range(len(boxes_pairs)):
	box1, box2 = boxes_pairs[i]

	if not uf.same_set(box1, box2):
		last_connection = [box1, box2]

	uf.union(box1, box2)


print("ANSWER:", boxes[last_connection[0]][0] * boxes[last_connection[1]][0])
