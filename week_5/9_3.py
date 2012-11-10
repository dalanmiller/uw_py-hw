fin = open('words.txt')

def avoids(avoided):
	print "Success"

def are_letters(word):
	print "Are letters!"
	return True

def are_unique(word):
	print "Are unique!"
	return True

def is_not_empty(word):
	if len(word) > 0:
		return True
	print "Your input must not be empty!"
	return False

def user_audit(word):
	if are_letters(word):
		if are_unique(word):
			if is_not_empty(word):
				return avoids(word)
	return user_input()

def user_input():
	avoided = raw_input('Please enter unique letters to avoid with no spaces:\n')
	user_audit(avoided)

user_input()
