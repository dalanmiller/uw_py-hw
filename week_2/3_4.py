#Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument.
def do_twice(f, your_value):
    f(your_value)
    f(your_value)

#Write a more general version of print_spam, called print_twice, that takes a string as a parameter and prints it twice.
def print_twice(your_string):
    print your_string
    print your_string

#Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
do_twice(print_twice, 'spam')

#Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter. There should be only two statements in the body of this function, not four.
def do_four(f, your_value):
    do_twice(f, your_value)
    do_twice(f, your_value)

do_four(print_twice, 'spam')
