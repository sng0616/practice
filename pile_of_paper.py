#Source: http://www.reddit.com/r/dailyprogrammer/comments/35s2ds/20150513_challenge_214_intermediate_pile_of_paper/

input = "20 10\n1 5 5 10 3\n2 0 0 7 7"

def split_vals(input):
# Where input is at least 2 lines of text with first line being 2 integers and following lines of 5 integers
	papers = []
	papers_val = []
	keys = ["canvas", "pile"]
	papers_dict = dict.fromkeys(keys, [])
	line_split = input.split("\n")
	enume = enumerate(line_split)
	for i, j in enume:
		colors = line_split[i].split(" ")
		papers = papers + colors
		color_val = [int(val) for val in colors]
		papers_val.append(color_val)
		if i == 0:
			papers_dict['canvas'] = color_val
		else:
			papers_dict['pile'].append(color_val)
#	print papers_val
#	print papers_dict
	return papers_dict, papers_dict["canvas"], papers_dict["pile"]

canvas = split_vals(input)[1]
paint = split_vals(input)[2]

print canvas, paint

#def create_pic(canvas):
grid = ''
for x in range(canvas[1]):
	grid = grid + "\n" + "0"*canvas[0]
#	return grid

print grid

def paint_pic(canvas, paint):
	for x in range(canvas[1]):
#		print "0"*canvas[0]
		for y in paint:
			for i, j in enumerate(paint):
				color = j[0]
				start_row = j[1]
				start_col = j[2]
				rows = j[3]
				col = j[4]
#	for k in range(col):
				if x in range(start_col, start_col+rows):
					print "0"*start_row + str(color)*rows + "0"*(canvas[0]-start_row-rows)
#				else:
#					print "0"*canvas[0]
#		print "0"*canvas[0]	
	return
	
paint_pic(canvas, paint)
	
# To-do list:
# 1. Create function to "paint" on canvas and keep *blank* spaces