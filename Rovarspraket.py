#!/usr/bin/env python
# coding: utf-8

# Source: http://www.reddit.com/r/dailyprogrammer/comments/341c03/20150427_challenge_212_easy_r%C3%B6varspr%C3%A5ket/

phrase = u"Tre Kronor är världens bästa ishockeylag."
vowels = "AaEeIiOoUuYy"
vowels2 = u"\xc4\xc5\xe4\xe5\xd6\xf6"
punct = ".?!:,@#$%^&*()[]{}<>`~"
extra = ""
rovar = ""

#print vowels, vowels2

for j in phrase:
# Taking vowels and spaces between words into account.
	if j in vowels or j in vowels2 or j in punct or j == " ":
		rovar = rovar + j
	else: 
		extra = j + "o" + j
		rovar = rovar + extra
		
print rovar

# Decode Rovarspraket

phrase_rovar = "ToTrore KoKrorononoror äror vovärorloldodenonsos bobäsostota isoshohocockokeylolagog."
enume_rovar = enumerate(phrase_rovar)
derovar = ""

for x, y in enume_rovar:
#	print x, y
	if y == "o" and phrase_rovar[x] + phrase_rovar[x+1] == "o" + phrase_rovar[x-1]:
		enume_rovar.next()
		continue		
	else: 
		derovar = derovar + y
print derovar
