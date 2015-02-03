# Source Inspiration: http://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/

# Description: ISBN's (International Standard Book Numbers) are identifiers for books. Given the correct sequence of digits, one book can be identified out of millions of others thanks to this ISBN. But when is an ISBN not just a random slurry of digits? That's for you to find out.

# Rules: Given the following constraints of the ISBN number, you should write a function that can return True if a number is a valid ISBN and False otherwise.
# An ISBN is a ten digit code which identifies a book. The first nine digits represent the book and the last digit is used to make sure the ISBN is correct.
# To verify an ISBN you :-
#obtain the sum of 10 times the first digit, 9 times the second digit, 8 times the third digit... all the way till you add 1 times the last digit. If the sum leaves no remainder when divided by 11 the code is a valid ISBN.
#For example :
#0-7475-3269-9 is Valid because
#(10 * 0) + (9 * 7) + (8 * 4) + (7 * 7) + (6 * 5) + (5 * 3) + (4 * 2) + (3 * 6) + (2 * 9) + (1 * 9) = 242 which can be divided by 11 and have no remainder.
#For the cases where the last digit has to equal to ten, the last digit is written as X. For example 156881111X.

pros_Str = raw_input("Please enter a 10-digit or a 13- digit ISBN. (No dashes) ")
pros_Str = pros_Str.replace("-", "")
enume = enumerate(pros_Str)
product_Sum = 0
last_digit = 0
last_ISBN = 0 

#print pros_Str

def ISBN13(pros_Str):
	product_Sum = 0
	for i, j in enume:
		if j == "X":
			j = "10"
		i+=1
		if i%2 == 0:
			mult = 3
		if i%2 == 1:
			mult = 1
		product = mult * int(j)
		product_Sum+=product
		print "{0} * {1} = {2}" .format(mult, j, product)

#	print product_Sum

	remains = product_Sum%10
#	last_digit = 10 - remains
#	last_ISBN = int(pros_Str[-1])

	if pros_Str[-1] != "X":	
		last_digit = 10 - remains
		last_ISBN = int(pros_Str[-1])
	else:
		last_digit = "X"
		last_ISBN = pros_Str[-1]

#	print last_digit
#	print last_ISBN

	if last_digit == last_ISBN:
		print "This is a valid ISBN."
	else:
		print "This is not a valid ISBN."
	return
		
def ISBN10(pros_Str):
	product_Sum = 0
	for i, j in enume:
		k = 10 - i
		if j == "X":
			j = "10"
		product = int(k) * int(j)
		product_Sum+=product
		print "{0} * {1} = {2}" .format(k, j, product)

#	print product_Sum

	remains = product_Sum%11

	if remains != 0:
		print "This is not a valid ISBN."
	else:
		print "This is a valid ISBN."
	return

if len(pros_Str) == 13:
	ISBN13(pros_Str)	
elif len(pros_Str) == 10:
	ISBN10(pros_Str)		
else:
	print "This is not a valid ISBN."
