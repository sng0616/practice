# Create a function/program to add 4 spaces to each line of code so it can be made into a comment on Reddit

fileName = raw_input("Which file would you like to convert? ")
if "." not in fileName:
	fileName = raw_input("Your file name is missing a suffix. Which file would you like to convert? ")
txtFile = raw_input("What would you like the text file to be called? ") + ".txt"

def Code2Text(fileName, txtFile):
	with open(fileName, "r") as openFile:
		splitFile = openFile.read().split("\n")
		with open(txtFile, "w") as newTextFile:
			newText = ""
			enume = enumerate(splitFile)
			for i, j in enume:
				if j.startswith("#"):
					enume.next()
					continue
				else:
					j = "    " + j
					newText = newText + "\n" + j	
			newTextFile.write(newText)	
	return newTextFile
	
Code2Text(fileName, txtFile)