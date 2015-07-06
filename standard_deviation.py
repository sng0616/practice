# Source: http://www.reddit.com/r/dailyprogrammer/comments/35l5eo/20150511_challenge_214_easy_calculating_the/

# Finds population standard deviation (as opposed to sample std dev)

from __future__ import division 
import math

numbers = "266 344 375 399 409 433 436 440 449 476 502 504 530 584 587"
list = numbers.split(" ")
sqr_total = 0
num_list = []

for i in list:
	i = int(i)
	num_list.append(i)

mean = sum(num_list)/len(num_list)

for i in list:
	diff = int(i) - mean
	square = (int(i) - mean)**2
	sqr_total = sqr_total + square

variance = sqr_total/len(list)
std_dev = round(math.sqrt(variance), 4)

print std_dev