def main():
	""" 
	For day three of adventofcode.com's calendar.
	"""
	# Get string of directions from input.txt
	dirs = open('input.txt','r').readlines()[0][:-1]

	# Part 1
	print "# of houses houses visited the first year: %d." \
		% len(enum_visited(dirs))

	# Part 2
	print "# of houses houses visited the second year: %d." \
		% len(enum_visited(dirs[::2]).union(enum_visited(dirs[1::2])))


def enum_visited(directions):
	"""
	Returns the set of visited (x, y) coordinates.
	""" 
	x, y, visited = 0, 0, set()

	# Iterate through each character in directions
	for direction in directions:
		visited.add((x, y))
		if direction == "^": 	(x, y) = (x, y + 1)
		elif direction == "<": 	(x, y) = (x - 1, y)
		elif direction == ">": 	(x, y) = (x + 1, y)
		elif direction == "v": 	(x, y) = (x, y - 1)

	return visited


if __name__ == "__main__":
    main()
