def count_at(word, letter, start):
	index = start
	count = 0
	while index < len(word):
		if word[index] == letter:
			count = count + 1
		index = index + 1
	return count

# Test queries
print count_at('banana', 'a', 0)
print count_at('banana', 'a', 3)
print count_at('university', 'i', 4)
print count_at('team', 'i', 0)
