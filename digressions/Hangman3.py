import urllib
from random import randint

wordSource = "http://www.mieliestronk.com/corncob_lowercase.txt"

WordReq = urllib.urlopen(wordSource)
wordList = WordReq.read().split("\n")
numbered = enumerate(wordList)
wordListE = []
wordListM = []
wordListH = []
randWordIndex = 0
randWord = ""

level = ""

#def choose_level(level):
level = raw_input("What level do you want? (Easy, Medium, Hard) ")
# Easy Level
if level == "Easy":
	for i, j in numbered:
		j = j.strip()
		if len(j) <= 6:
			wordListE.append(wordList[i])
	randWordIndex = randint(0, len(wordListE))	
	randWord = wordListE[randWordIndex].strip()

# Medium Level
if level == "Medium":
	for i, j in numbered:
		j = j.strip()
		if len(j) > 6 and len(j) <=10:
			wordListM.append(wordList[i])
	randWordIndex = randint(0, len(wordListM))	
	randWord = wordListM[randWordIndex].strip()

# Hard Level
if level == "Hard":
	for i, j in numbered:
		j = j.strip()
		if len(j) > 10:
			wordListH.append(wordList[i])
	randWordIndex = randint(0, len(wordListH))	
	randWord = wordListH[randWordIndex].strip()
print randWord
#	return randWord

randWordLow = randWord.lower()
randWordLen = len(randWord)
letterNo = enumerate(randWord)
empty = "_ " * randWordLen

print "This word has {0} letters." .format(randWordLen)
print empty

guessLett = raw_input("Guess a letter. ")[0]
guessList = []
missedList = []
correctList = []

def checkGuess(guessLett):
	if guessLett.isalpha() == False:
		guessLett = raw_input("That was not a letter. Please guess a letter. ")[0]
	if guessLett in guessList:
		guessLett = raw_input("You already guessed that letter. Please guess another letter. ")[0]
	return 

# def printLinesLists():
# 	for i in range(randWordLen):
# 		if randWord[i] in correctList:
# 			empty = empty[:i*2]+randWord[i]+" "+empty[(i+1)*2:]
# 		print empty[:randWordLen*2]
# 		print correctList
# 		print missedList
# 	if guessLett in randWord:
# 		guessLett = raw_input("Good guess. Try again. ")
# 	else:
# 		guessLett = raw_input("No dice. Try again. ")
# 	return

while len(missedList) < 6:
	checkGuess(guessLett)
	if guessLett in randWord:
		guessList.append(guessLett)
		correctList.append(guessLett)
		if sorted(set(wordList)) == sorted(set(correctList)):
			print "The word was {0}. You won!" .format(randWord)
			break 
		else:
			for i in range(randWordLen):
				if randWord[i] in correctList:
					empty = empty[:i*2]+randWord[i]+" "+empty[(i+1)*2:]
			print empty[:randWordLen*2]
			print correctList
			print missedList
			guessLett = raw_input("Good guess. Try again. ")
	if guessLett not in randWord:
		guessList.append(guessLett)
		missedList.append(guessLett)
		if len(missedList) == 6:
			print "The word was {0}. You lose." .format(randWord)
		else:
			for i in range(randWordLen):
				if randWord[i] in correctList:
					empty = empty[:i*2]+randWord[i]+" "+empty[(i+1)*2:]
			print empty[:randWordLen*2]
			print correctList
			print missedList
			guessLett = raw_input("No dice. Try again. ")

# To-Do List:
# 1. Write function to choose level.
# 2. Write function to reduce repetition in the while loop.