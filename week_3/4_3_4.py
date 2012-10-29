from swampy.TurtleWorld import *
import math

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

def circle(t, r):
	radius = r/13
	polygon(t, 90, radius)

world = TurtleWorld()
bob = Turtle()
print bob

bob.delay = 0.01
circle(bob, 100)

wait_for_user()
