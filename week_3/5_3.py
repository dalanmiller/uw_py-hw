def check_fermat (a, b, c, n):
	if n <= 2:
		n = raw_input('Please enter a value for integer n that is greater than 2:\n')
		n = int(n)
		check_fermat(a, b, c, n)
	else:
		print('Now checking values ' + str(a) + ', ' + str(b) + ', ' + str(c) + ', and ' + str(n) + '...')
		if (a**n) + (b**n) == (c**n):
			print "\nHoly smokes, Fermat was wrong!"
		else:
			print "\nNo, that doesn't work.\n"
			user_input()

def user_input():
	print "Are you prepared to prove Fermat wrong?"
	a = raw_input('Please enter a value for integer a:\n')
	a = int(a)
	b = raw_input('Please enter a value for integer b:\n')
	b = int(b)
	c = raw_input('Please enter a value for integer c:\n')
	c = int(c)
	n = raw_input('Please enter a value for integer n that is greater than 2:\n')
	n = int(n)
	check_fermat(a, b, c, n)

user_input()
