def count_all_paths(graph, start, end):
	memo = {}
	for key, values in graph.items():
		memo[key] = None
		for val in values:
			memo[val] = None
	memo[end] = 1

	while memo[start] is None:
		for node in memo:
			if memo[node] is None and all(memo[child] is not None for child in graph.get(node, ())):
				memo[node] = sum(memo[child] for child in graph.get(node, ()))

	return memo[start]
