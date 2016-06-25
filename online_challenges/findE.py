#Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program generate e up to that many decimal places. Keep a limit to how far the program will go. Source: https://github.com/karan/Projects

import math

nInput = raw_input("How many decimal places of e? ")

while nInput.isdigit() == False:
	print "That is not a number."
	nInput = raw_input("Please submit a number. ")

if nInput.isdigit() == True:
	inputDigit = int(nInput) + 2
	actualE = str(math.e)[2:inputDigit]
	print "e to the nth place where n = {0}: 2.{1}" .format(nInput, actualE)