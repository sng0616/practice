# Project idea at http://www.pbs.org/idealab/2014/07/5-fun-programming-projects-to-help-learn-python/

import random

correctNo = random.randint(1,5)

guessNo = int(raw_input("What number am I thinking of? "))

while guessNo != correctNo:
	if guessNo < correctNo:
		guessNo = int(raw_input("Nope. Too low. Guess again. "))
#		print correctNo
	if guessNo > correctNo:
		guessNo = int(raw_input("Nope. Too high. Guess again.  "))
#		print correctNo
else:
	print "Congratulations! You win absolutely nothing. You're welcome."