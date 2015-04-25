# Source: http://www.reddit.com/r/dailyprogrammer/comments/32goj8/20150413_challenge_210_easy_intharmonycom/

from __future__ import division 

def checkNumber(input):
	if input.isdigit() == False:
		input = raw_input("That was not a number. Please enter an integer. ")
	if "." in input:
		input = raw_input("That number contained a decimal point. Please enter an integer. ")
	else:
		pass
print "Please enter 2 integers."
input1 = int(raw_input("Number #1: "))
input2 = int(raw_input("Number #2: "))

input1b = bin(input1)[2:]
input2b = bin(input2)[2:]

#print input1b, input2b

#Are these inputs the same length?
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
print input1b0, input2b0

#What is the opposite of both inputs?

def switchCharacters(input1b0):
	opposite = ""
	enume = enumerate(input1b0)
	for i, j in enume:
#		print i, j
		if j == "0":
			opposite = opposite + "1"
		else: 
			opposite = opposite + "0"
#	print opposite
	oppositeDec = int(opposite, 2)
	return oppositeDec

opposite1 = switchCharacters(input1b0)
opposite2 = switchCharacters(input2b0)
#print oppositeBin1, oppositeBin2

zipped =zip(input1b0, input2b0)
total = len(input1b0)

#Are these inputs the same number?
if input1b0 == input2b0:
	print "These numbers are a 100% match... but only because they're the same number. \n This number should avoid {0}" .format(opposite1)
else:
	pointSim = 0
#How similar are they? How many digits do they have in common?
	for i, j in zipped:
#		print i, j
		if i == j:
			pointSim = pointSim + 1
#			print pointSim
		else:
			pointSim = pointSim
	divided = round(pointSim*100/total)
	match = str(int(divided))
	print "These numbers are a {0}% match. \n {1} should avoid {2}. \n {3} should avoid {4}." .format(match, input1, opposite1, input2, opposite2 )
