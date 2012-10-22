from swampy.TurtleWorld import *

def square(t, length):
	"Draws a square of (turtle, length)"
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, n, length):
	"Tells (turtle) to draw an (n)-sided shape of (length)"
	for i in range(n):
		fd(t, length)
		lt(t, 360/n)

world = TurtleWorld()
bob = Turtle()
print bob

polygon(bob, 8, 50)

wait_for_user()
