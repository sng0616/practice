import urllib

wordSource = "http://randomword.setgetgo.com/get.php"

WordReq = urllib.urlopen(wordSource)
randWord = WordReq.read().strip()
randWordLow = randWord.lower()
randWordLen = len(randWord)
wordList = list(randWord)
letterNo = enumerate(randWord)

level = raw_input("What level do you want? (Easy or Hard) " )

# Easy Level
#if level == "Easy" and randWordLen > 7:
if level == "Easy":
	while randWordLen > 10:
		WordReq = urllib.urlopen(wordSource)
		randWord = WordReq.read().strip()

# Medium Level
#if level == "Medium" and randWordLen < 7 and randWordLen < 10:
#if level == "Medium":	
#	while randWordLen < 7 or randWordLen > 10:
#		WordReq = urllib.urlopen(wordSource)
#		randWord = WordReq.read().strip()
		
# Hard Level
#if level == "Hard" and randWordLen < 10:
if level == "Hard":
	while randWordLen < 10:
		WordReq = urllib.urlopen(wordSource)
		randWord = WordReq.read().strip()

print randWord
