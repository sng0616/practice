import urllib
from random import randint

wordSource = "http://www.mieliestronk.com/corncob_lowercase.txt"

WordReq = urllib.urlopen(wordSource)
wordList = WordReq.read().split("\n")
numbered = enumerate(wordList)

randWordIndex = 0
randWord = ""

def assign_list(level, numList):
    wordListE = []
    wordListM = []
    wordListH = []
    for i, j in numList:
        j = j.strip()
        if len(j) <= 6:
            wordListE.append(j)
        elif len(j) > 6 and len(j) <= 10:
            wordListM.append(j)
        else:
            wordListH.append(j)
    if level == 'Easy':
        return wordListE
    elif level == 'Medium':
        return wordListM
    else:
        return wordListH
        
level = raw_input("What level do you want? (Easy, Medium, Hard) ")

myList = assign_list(level, numbered)
randWordIndex = randint(0, len(myList))	
randWord = myList[randWordIndex].strip()
    
print randWord
#	return randWord

randWordLow = randWord.lower()
randWordLen = len(randWord)
letterNo = enumerate(randWord)
empty = "_ " * randWordLen

print "This word has {0} letters." .format(randWordLen)
print empty

guessLett = raw_input("Guess a letter. ")[0].lower()
guessList = []
missedList = []
correctList = []

def checkGuess(guessLett):
	if guessLett.isalpha() == False:
		guessLett = raw_input("That was not a letter. Please guess a letter. ")[0].lower()
	if guessLett in guessList:
		guessLett = raw_input("You already guessed that letter. Please guess another letter. ")[0].lower()
	return 

while len(missedList) < 6:
	checkGuess(guessLett)
	if guessLett in randWord:
		guessList.append(guessLett)
		correctList.append(guessLett)
		if sorted(set(list(randWord))) == sorted(set(correctList)):
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

            