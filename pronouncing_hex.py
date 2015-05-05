# Source: http://www.reddit.com/r/dailyprogrammer/comments/34rxkc/20150504_challenge_213_easy_pronouncing_hex/

# !/usr/bin/python

hex_dict = {"0xA0":"Atta", "0xB0":"Bibbity", "0xC0":"City", "0xD0":"Dickety", "0xE0":"Ebbity", "0xF0":"Fleventy"} 
numbers = {"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}

#for m, n in HexDict.items():
#	print m, n 

hex_value = "0xDAF1"
hex_call4 = hex_value[:3]+"0"
hex_call6 = hex_value[:3]+"000"
hex_digit = hex_value[3:]
word_digit = ""

#print hex_call, hex_digit

if len(hex_value) == 4 and hex_call4 in hex_dict:
	print hex_dict[hex_call], numbers[hex_digit]
elif len(hex_value) == 6 and hex_call4 in hex_dict:
	for i in hex_digit:
		print i
		if i == "0":
			continue
		elif i.isdigit() == True: 
			word_digit = word_digit + " " + numbers[i]
		else:
			hex_call = "0x"+i+"0"
			word_digit = word_digit + " " + hex_dict[hex_call]
	print hex_dict[hex_call4] + " " + "bitey" " " + word_digit
else:
	print "That was not a hexidecimal."
	
# To-do list (ROUGH DRAFT):
#
# 1. Fix conditions/values for higher place hex values