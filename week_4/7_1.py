def print_n(s, n):
	"Prints a string (s) n times using recursion."
	if n <= 0:
		return
	print s
	print_n(s, n-1)

def print_n_reloaded(s, n):
	"'Improved' print_n() that uses iteration."
	while n > 0:
		print s
		n = n - 1
