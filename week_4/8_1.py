def esrever(s):
	"Takes a string as an argument and displays the letters backward, one per line."
	index = len(s)
	while index > 0:
		letter = s[index - 1]
		print letter
		index = index - 1

esrever('banana')
