# Source Inspiration: http://www.reddit.com/r/dailyprogrammer/comments/2s7ezp/20150112_challenge_197_easy_isbn_validator/

#Bonus: Write an ISBN generator. That is, a programme that will output a valid ISBN number (bonus if you output an ISBN that is already in use :P )
from random import randint

ISBN_len = int(raw_input("Are you looking for a 10-digit or a 13-digit ISBN? (10/13) "))
n = ISBN_len - 1

def ndigits_rand(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

pros_ISBN = str(ndigits_rand(n))
#pros_ISBN = "855911054"
print pros_ISBN
enume = enumerate(pros_ISBN)

def gen_10(pros_ISBN):
	product_Sum = 0
	check_digit = 0
	for i, j in enume:
		k = 10 - i
		if j == "X":
			j = "10"
		product = int(k) * int(j)
		product_Sum+=product
		print "{0} * {1} = {2}" .format(k, j, product)

#	print product_Sum

	remains = product_Sum%11
	print remains
	if remains != 0:
		check_digit = str(11 - remains)
		if check_digit == "10":
			check_digit = "X"
	else:
		check_digit = "0"
	pros_ISBN+=check_digit
	return pros_ISBN	
#print gen_10(pros_ISBN)

def gen_13(pros_ISBN):
	product_Sum = 0
	check_digit = 0
	for i, j in enume:
#		print i, j
		if i%2 == 1:
			k = 3
		if i%2 == 0:
			k = 1
		if j == "X":
			j = "10"
		product = k*int(j)
		product_Sum+=product
		print "{0} * {1} = {2}" .format(k, j, product)

	print product_Sum

	remains = product_Sum%10
#	print remains
	if remains != 0:
		check_digit = str(11 - remains)
		if check_digit == "10":
			check_digit = "X"
	else:
		check_digit = "0"
	pros_ISBN+=check_digit
	return pros_ISBN
	
if ISBN_len == 10:
	print gen_10(pros_ISBN)	
elif ISBN_len == 13:
	print gen_13(pros_ISBN)