fin = open('words.txt')

def avoids(avoided):
	for line in fin:
		passes_filter = True
		word = line.strip()
		for letter in avoided:
			if letter in word:
				passes_filter = False
		if passes_filter:
			print word

def is_not_empty(word):
	"Verifies user input is not empty."
	if len(word) > 0:
		return True
	print "Your input must not be empty!"
	return False

def user_audit(word):
	# Removed the check for alphabetical input until I learn lists and tuples
	# Removed the check for unique letters until I learn lists and tuples
	if is_not_empty(word):
		return avoids(word)
	return user_input()

def user_input():
	avoided = raw_input('Please enter unique letters to avoid:\n')
	avoided = avoided.strip()	#Removes whitespace from beginning and end of input
	avoided = avoided.replace(" ", "")	#Removes spaces from inside string
	avoided = avoided.lower()	#Forces letters to become lowercase
	user_audit(avoided)

user_input()
