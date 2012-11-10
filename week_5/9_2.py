fin = open('words.txt')

def has_no_e(word):
	"Evaluates as True if a word does not contain the letter 'e'"
	return 'e' not in word

word_count = 0
word_has_no_e = 0

for line in fin:
	word = line.strip()
	word_count += 1
	if has_no_e(word):
		word_has_no_e += 1

print ("%s%s of %s words do not contain the letter 'e'"
	% (float(word_has_no_e) / float(word_count) * 100, '%', word_count))
