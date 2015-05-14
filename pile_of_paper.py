#Source: http://www.reddit.com/r/dailyprogrammer/comments/35s2ds/20150513_challenge_214_intermediate_pile_of_paper/

input = "20 10\n1 5 5 10 3\n2 0 0 7 7"
line_split = input.split("\n")
input_num = []

print line_split

canvas = "20 10"
canvas_val = [int(val) for val in canvas.split(" ")]
#print canvas_val

def create_canvas(canvas_val):
	for x in range(canvas_val[1]):
		print "0"*canvas_val[0]
	return
	
create_canvas(canvas_val)

paint = "1 5 5 10 3\n2 0 0 7 7"
paint_lines = [i for i in paint.split("\n")]

print paint_lines