from swampy.TurtleWorld import *

def square(turtle, length):
    for i in range(4):
        fd(turtle, length)
        lt(turtle)
        
def polygon(turtle, length):
    for i in range(4):
        fd(turtle, length)
        lt(turtle)

world = TurtleWorld()
bob = Turtle()

square(bob, 500) #goes off screen

wait_for_user()
