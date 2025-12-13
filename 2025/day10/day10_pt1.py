with open("input.txt", "r") as file:
	machines = [m.split(" ") for m in file.read().splitlines()]

lights_lst = [[False if c == "." else True for c in m[0][1:-1]] for m in machines]
buttons_lst = [[[int(n) for n in c[1:-1].split(",")] for c in m[1:-1]] for m in machines]
joltage_lst = [[int(n) for n in m[-1][1:-1].split(",")] for m in machines]


def press_button(lights: list, button):
	pressed_lights = lights.copy()
	for n in button:
		pressed_lights[n] = not pressed_lights[n]
	return pressed_lights

def get_min_presses(lights: list, buttons):
	visited_lights = set()
	queued_lights = [(tuple(lights), 0)]

	while queued_lights:
		current_lights, level = queued_lights.pop(0)
		if current_lights not in visited_lights:
			visited_lights.add(current_lights)

			if all(l == False for l in current_lights):
				return level

			for btn in buttons:
				queued_lights.append((tuple(press_button(list(current_lights), btn)), level+1))


presses_total = 0

for lights, buttons in zip(lights_lst, buttons_lst):
	presses_total += get_min_presses(lights, buttons)

print("ANSWER:", presses_total)
