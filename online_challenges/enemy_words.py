# Source: https://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/

# Okay so there is a valley. On each side you got cannons. They are firing words at each other. In the middle of the valley the words would make contact and explode. Similar letters from each word would cancel out. But the left over unique letters from each word would fall to the valley and slowly fill it up.

# So your challenge is to come up with the code given two words you eliminate letters in common at a ratio of 1 for 1 and produce a set of letters that are left over from each word after colliding in mid air. Which ever side has the most letters left over "wins". If each side donates an equal amount of letters it is a "tie".

L_word = "because"
R_word = "cause"

L_points = 0
R_points = 0

word_combo = L_word + R_word
set_letters = list(set(word_combo))
no_dupe = []

print set_letters
print type(set_letters)

# Add rule/statement such that numbers are eliminated in a 1:1 ratio. No '2 birds, 1 letter'.

for i in range(0, len(set_letters)):
	if set_letters[i] not in L_word:
		no_dupe.append(set_letters[i])
		L_points+=1
		if 
	if set_letters[i] not in R_word:
		no_dupe.append(set_letters[i])
		R_points+=1

print set_letters
print no_dupe
print L_points
print R_points
	