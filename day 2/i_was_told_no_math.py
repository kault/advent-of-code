def main():
	""" For day two of adventofcode.com's calendar. """

	surface_area = 0
	ribbon = 0

	with open('input.txt','r') as input_file:
		for dimensions in input_file.readlines():
			dim_list = map( int, dimensions.strip().split("x") )
			[l,w,h] = dim_list
			surface_area += 2*l*w + 2*w*h + 2*h*l + (l*w*h/max([l,w,h]))

			min_dim = min(dim_list)
			dim_list.remove(min_dim)
			next_min_dim = min(dim_list)
			ribbon += (2 * min_dim + 2 * next_min_dim) + (l * w * h)


	print "Surface area for elves to order: %d square feet." % surface_area 
	print "Amount of ribbon to buy: %d feet." % ribbon


if __name__ == "__main__":
	main()