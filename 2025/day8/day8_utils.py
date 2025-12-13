class UnionFind:
	def __init__(self, size):
		self.parent = [i for i in range(size)]
		self.rank = [1] * size

	def find(self, x):
		if x != self.parent[x]:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		rootX = self.find(x)
		rootY = self.find(y)
		if rootX != rootY:
			if self.rank[rootX] > self.rank[rootY]:
				self.parent[rootY] = rootX
			elif self.rank[rootX] < self.rank[rootY]:
				self.parent[rootX] = rootY
			else:
				self.parent[rootY] = rootX
				self.rank[rootX] += 1

	def same_set(self, x, y):
		return self.find(x) == self.find(y)

def rank_distance(coords1, coords2):
	return (
		(coords1[0] - coords2[0])**2 +
		(coords1[1] - coords2[1])**2 +
		(coords1[2] - coords2[2])**2
	)
