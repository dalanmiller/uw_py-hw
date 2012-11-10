# Modify your program from the previous section to print only
# the words that have no "e" and compute
# the percentage of the words in the list have no "e."

fin = open('words.txt')

def has_no_e(word):
	"Evaluates as True if a word does not contain the letter 'e'"
	for letter in word:
		if letter is 'e':
			return False
	return True

word_count = 0
word_has_no_e = 0

for line in fin:
	word = line.strip()
	word_count = word_count + 1
	if has_no_e(word):
		word_has_no_e = word_has_no_e + 1

print str(float(word_has_no_e) / word_count * 100) + "% of " + str(word_count) + " words do not contain the letter 'e'"
