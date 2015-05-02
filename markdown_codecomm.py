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
			for i in splitFile:
				i = "    " + i
				newText = newText + "\n" + i	
			newTextFile.write(newText)	
	return newTextFile
	
Code2Text(fileName, txtFile)