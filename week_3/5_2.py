def winning():
	"Duh, WINNING!"
	print "WINNING"

def losing():
	"Duh, LOSING!"
	print "LOSING"

def do_n (myFunc, n):
	"Takes a function object and a number, n, as arguments, and that calls the given function n times."
	if n <= 0:
		return
	else:
		myFunc()
		n = n - 1
		do_n(myFunc, n)

do_n(winning, 3)
do_n(losing, 2)