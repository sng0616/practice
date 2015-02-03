# Source: http://www.pbs.org/idealab/2014/07/5-fun-programming-projects-to-help-learn-python/

import random

print "Roll the die!"
chance = random.randint(1,6)
print "You rolled {0}." .format(chance)
roll = raw_input("Would you like to roll again? (Y/N) ")
while roll == "Y":
	chance = random.randint(1,6)
	print "You rolled {0}." .format(chance)
	roll = raw_input("Would you like to roll again? (Y/N) ")
else:
	print "Kthxbye"