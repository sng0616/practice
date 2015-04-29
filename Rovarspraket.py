# Source: http://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/

phrase = "Purple"
enume = enumerate(phrase)
extra = ""
rovar = ""

for i, j in enume:
	if j in 'aeiouy':
		rovar = rovar + j
	else: 
		extra = j + "o" + j
		rovar = rovar + extra
print rovar

# To-do list:
# 1. Add considerations for non-ASCII characters