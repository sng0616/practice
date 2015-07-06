# Source: http://www.reddit.com/r/dailyprogrammer/comments/34rxkc/20150504_challenge_213_easy_pronouncing_hex/

# !/usr/bin/python

hex_dict = {"A":"atta", "B":"bibbity", "C":"city", "D":"dickety", "E":"ebbity", "F":"fleventy"} 
numbers = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
letters = {"A":"ay", "B":"bee", "C":"see", "D":"dee", "E":"ee", "F":"eff"} 

#for m, n in HexDict.items():
#	print m, n 

hex_value = "0xDAF1"
hex_call4 = hex_value[:3]+"0"
hex_call6 = hex_value[:3]+"000"
hex_digit = hex_value[2:]
enume_hex = enumerate(hex_digit)
word_digit = ""

#print hex_call, hex_digit

# def find_word_digit(hex_value):
# 
# 	return word_digit

for i, j in enume_hex:
	print i, j
	if j == "0":
			continue
	elif len(hex_value) > 4:
		if i % 2 == 0:
			if j.isdigit() == True: 
				word_digit = word_digit + " bitey " + numbers[j]
			else:
				word_digit = word_digit + " bitey " + hex_dict[j]
		else:
			if j.isdigit() == True: 
				word_digit = word_digit + " " + numbers[j]
			else:
				word_digit = word_digit + " " + hex_dict[j]
	else:
		if j.isdigit() == True: 
			word_digit = word_digit + " " + numbers[j]
		else:
			word_digit = word_digit + " " + hex_dict[j]
print word_digit[7:]
	
# To-do list (ROUGH DRAFT):
#
# 1. Fix conditions/values for first two characters in higher place hex values
# 2. Create break for inappropriate input ("This is not a hex value.").
# 3. Incorporate letters dictionary in statements