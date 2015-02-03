# Source: https://www.interviewcake.com/question/product-of-other-numbers

from operator import mul

numbers_list = [2,3,4,5,6]
mul_list = []
#print type(numbers_list)
product_list = []
numbered = enumerate(numbers_list)

for i, j in numbered:
	mul_list = numbers_list.pop(i)
	print mul_list
	product = reduce(mul, numbers_list)
	product_list.append(product)
#	list = list.insert(i, j)

print product_list
