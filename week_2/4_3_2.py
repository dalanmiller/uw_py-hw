from swampy.TurtleWorld import *

def square(t, length):
	"Draws a square of (turtle, length)"
	for i in range(4):
		fd(t, length)
		lt(t)

world = TurtleWorld()
bob = Turtle()
print bob

square(bob, 190)

wait_for_user()
