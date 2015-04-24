# Source: http://www.reddit.com/r/dailyprogrammer/comments/32goj8/20150413_challenge_210_easy_intharmonycom/

from __future__ import division 

input1 = int(raw_input("Input 1: "))
input2 = int(raw_input("Input 2: "))

input1b = bin(input1)[2:]
input2b = bin(input2)[2:]

# input1b0 = ""
# input2b0 = ""

#print input1b, input2b
# Are these inputs the same length?
def sameDigits(input1b, input2b):
	if len(input1b) < len(input2b):
		difference = len(input2b) - len(input1b)
		input1b = "0" * difference + input1b
	else:
		difference = len(input1b) - len(input2b)
		input2b = "0" * difference + input2b
	return input1b, input2b

input1b0 = sameDigits(input1b, input2b)[0]
input2b0 = sameDigits(input1b, input2b)[1]

# What is the opposite of both inputs?

print input1b0, input2b0
zipped =zip(input1b0, input2b0)

total = len(input1b0)
#match = str(int((pointSim/total) * 100))
# Are these inputs the same number?
if input1b0 == input2b0:
	print "These numbers are a 100% match... but only because they're the same number."
else:
	pointSim = 0
# How similar are they? How many digits do they have in common?
	for i, j in zipped:
		print i, j
		if i == j:
			pointSim = pointSim + 1
			print pointSim
		else:
			pointSim = pointSim
	divided = round(pointSim*100/total)
	match = str(int(divided))
	print "These numbers are a {0}% match." .format(match)

# How many digits in common?