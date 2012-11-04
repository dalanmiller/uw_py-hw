def eval_loop():
	"""
	Iteratively prompts the user, takes the resulting input
	and evaluates it using eval, and prints the result.

	Continues until the user enters 'done', and then returns
	the value of the last expression it evaluated.
	"""
	while True:
		line = raw_input('Evaluate > ')
		if line == 'done':
			print "Done!"
			break
		else:
			print line + '...'
		print str(eval(line)) + '\n'

eval_loop()
