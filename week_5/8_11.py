def any_lowercase1(s):
	"Checks to see if the first letter is lowercase."
	for c in s:
		if c.islower():
			return True
		else:
			return False

def any_lowercase2(s):
	"Checks to see if the letter c is lowercase. Ignores input."
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'

def any_lowercase3(s):
	"Checks to see if the last letter is lowercase."
	for c in s:
		flag = c.islower()
	return flag

def any_lowercase4(s):
	"Checks to see if at least one letter is lowercase."
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

def any_lowercase5(s):
	"Checks to see if all letters are lowercase."
	for c in s:
		if not c.islower():
			return False
	return True

def user_test(s, n):
	"Allows user to pass string and test number as arguments."
	if n == 1:
		return any_lowercase1(s)
	elif n == 2:
		return any_lowercase2(s)
	elif n == 3:
		return any_lowercase3(s)
	elif n == 4:
		return any_lowercase4(s)
	elif n == 5:
		return any_lowercase5(s)
	else:
		return "Invalid test number"
