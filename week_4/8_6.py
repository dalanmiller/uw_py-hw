def count_at(word, letter, start):
	index = start
	count = 0
	while index < len(word):
		if word[index] == letter:
			count = count + 1
		index = index + 1
	return count

print count_at('banana', 'b', 0)
