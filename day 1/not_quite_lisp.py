def main():
	""" For day one of adventofcode.com's calendar. """
	with open('input.txt','r') as input_file:
		instructions = input_file.readlines()[0]

	print "Santa's instructions take him to floor %d." % part_1(instructions)
	print "He ends up in the basement on step %d." % part_2(instructions)


def part_1(instructions):
	""" Returns Santa's final floor after following all instructions. """
	return instructions.count("(") - instructions.count(")")


def part_2(instructions):
	""" Returns the (1-indexed) position of """
	floor, count = 0, 0

	for c in instructions:
		floor = (floor + 1) if c == "(" else (floor - 1) 
		count += 1
		if floor < 0: return count

	return count


if __name__ == "__main__":
    main()