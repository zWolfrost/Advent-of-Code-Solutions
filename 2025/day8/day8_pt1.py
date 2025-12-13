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


PAIRS_TO_CONNECT = 1000

uf = UnionFind(len(boxes))
for i in range(PAIRS_TO_CONNECT):
	box1, box2 = boxes_pairs[i]
	uf.union(box1, box2)


circuit_length = [0] * len(boxes)

for id in [uf.find(i) for i in range(len(boxes))]:
	circuit_length[id] += 1

circuit_length = sorted(circuit_length, reverse=True)


print("ANSWER:", circuit_length[0] * circuit_length[1] * circuit_length[2])
