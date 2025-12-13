
def get_norm_pixels(pixel1, pixel2):
	ul_pixel = (min(pixel1[0], pixel2[0]), min(pixel1[1], pixel2[1]))
	br_pixel = (max(pixel1[0], pixel2[0]), max(pixel1[1], pixel2[1]))

	return ul_pixel, br_pixel

def get_pixels_square(pixel1, pixel2):
	ul_pixel, br_pixel = get_norm_pixels(pixel1, pixel2)

	coords = set()

	for i in range(ul_pixel[0], br_pixel[0]+1):
		for j in range(ul_pixel[1], br_pixel[1]+1):
			coords.add((i, j))

	return coords

def get_pixels_interior_perimeter(pixel1, pixel2):
	ul_pixel, br_pixel = get_norm_pixels(pixel1, pixel2)

	ul_pixel = (ul_pixel[0] + 1, ul_pixel[1] + 1)
	br_pixel = (br_pixel[0] - 1, br_pixel[1] - 1)

	coords = []

	for i in range(ul_pixel[0], br_pixel[0]+1):
		coords.append((i, ul_pixel[1]))
		coords.append((i, br_pixel[1]))
	for i in range(ul_pixel[1], br_pixel[1]+1):
		coords.append((ul_pixel[0], i))
		coords.append((br_pixel[0], i))

	return coords
