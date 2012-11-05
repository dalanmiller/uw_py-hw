def count(word, letter):
	count = 0
	for s in word:
		if s == letter:
			count = count + 1
	print count

count('banana', 'a')	# There are 3 'a's in 'banana'
count('team', 'i')		# There is no 'i' in 'team'
