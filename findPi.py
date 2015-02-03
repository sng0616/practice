#Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go. Source: https://github.com/karan/Projects

import math

nInput = raw_input("How many decimal places of pi? ")

while nInput.isdigit() == False:
	print "That is not a number."
	nInput = raw_input("Please submit a number. ")

if nInput.isdigit() == True:
	inputDigit = int(nInput) + 2
	actualPi = str(math.pi)[2:inputDigit]
	print "Pi to the nth place where n = {0}: 3.{1}" .format(nInput, actualPi)