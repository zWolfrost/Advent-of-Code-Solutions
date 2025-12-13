from day11_utils import count_all_paths

with open("input.txt", "r") as file:
	data = file.read().splitlines()

graph = {}

for line in data:
	key, values = line.split(":")
	graph[key] = tuple(values.split())


print("ANSWER:",
	count_all_paths(graph, "svr", "fft") *
	count_all_paths(graph, "fft", "dac") *
	count_all_paths(graph, "dac", "out")
)
