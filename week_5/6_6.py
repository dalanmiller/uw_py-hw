# Exercise 6.6. A palindrome is a word that is spelled
# the same backward and forward, like "noon"
# and "redivider". Recursively, a word is a palindrome
# if the first and last letters are the same and the
# middle is a palindrome.
# 
# The following are functions that take a string argument
# and return the first, last, and middle letters:

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]
