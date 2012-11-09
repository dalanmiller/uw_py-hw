def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def test_three(word):
	print 'Now testing ' + word
	print first(word)
	print last(word)
	print middle(word) + '\n'

def user_test_1():
	"Test cases for 8_6 part 1"
	test_three('banana')
	test_three('redivider')
	test_three('tw')
	test_three('o')
	# test_three('')	# IndexError: string index out of range

def is_palindrome(word):
    if len(word) == 0:
    	return False
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print is_palindrome('banana')
print is_palindrome('redivider')
print is_palindrome('tw')
print is_palindrome('o')
print is_palindrome('')
