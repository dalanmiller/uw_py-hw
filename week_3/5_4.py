def is_triangle(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)
	if a > (b + c) or b > (a + c) or c > (a + b):
		print "\nNo\n"
		user_input()
	elif a == (b + c) or b == (a + c) or c == (a + b):
		print "\nYes (degenerate triangle)"
	else:
		print "\nYes"

def user_input():
	print "Let's find out if you know how to build a triangle."
	a = raw_input('Please enter a value for integer a:\n')
	a = int(a)
	b = raw_input('Please enter a value for integer b:\n')
	b = int(b)
	c = raw_input('Please enter a value for integer c:\n')
	c = int(c)
	is_triangle(a, b, c)

user_input()
