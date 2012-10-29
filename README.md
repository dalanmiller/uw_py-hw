# Stassi's UW Python Homework #

**Developer:** Andreas Stassivik  
**Instructor:** Jeff Silverman  
**Class:** Certificate Program in Python Programming (2012)

* [Course Overview](https://docs.google.com/document/pub?id=1HHAean0DWMK_Wh1PbGcyd8VqFFWjI4d-o50lBAlILus)
* [Book](http://www.greenteapress.com/thinkpython/)
* [Book (Interactive)](http://interactivepython.org/courselib/static/thinkcspy/index.html)
* [Problems](http://www.commercialventvac.com/python/index.html)
* [Presentation: Andreas' Python Applications](https://docs.google.com/presentation/pub?id=1zAHdFjKlDOk62n0kCZS4lUPH1Or79iyVnPUX94bSnlE&start=false&loop=false&delayms=15000)

## Week 3##
### Homework & Reading ###
#### Chapter 4 ####
* Due: 4, 5, 6, and 7
* After working on the initial exercises for a while and checking their answers, I am comfortable leaving Swampy and moving on to other exercises.
* Liked discovering the procedure for development plans:
  1. Write small program without function definitions
  1. Encapsulate program as function and name it
  1. Generalize function, add parameters
  1. Repeat prior steps, copypasta working code
  1. Refactor program's similar functions for efficiency

#### Chapter 5 ####
* Created an HTML template for stack diagrams
* 

### In-class ###
* Discussed conditionals, booleans
  * "Leave true and false alone!"
  * 0.0 is false float, 0 is false int
  * None does not equal true *or* false
  * A list containing "False" will still return True
* while loops are good for running functions indefinitely, for unpredictable iterables
* interation: continue is great for concise readability of code
* "for... else" is valid Python syntax
* Recursion allows functions to call themselves
  * Anything you can do with a loop you can do with recursion, and vice versa, but pick the method that works in context
  * Recursion is efficient for navigating binary trees (eg: r(r(r())) )
  * More examples:
    * Fibonacci sequence
    * 8 Queens problem
    * Fractual curves
    * Space-filling curves
* Floating point numbers are bad at division due to C back end, as seen in Quiz 2
  * Approach: abs(a-b) < delta * abs(a-b)

## Week 2 ##
### Homework & Reading ###
* Due: 1, 2, & 3
* Got Swampy installed!
* Started creating presentation about [how I plan on using Python](https://docs.google.com/presentation/pub?id=1zAHdFjKlDOk62n0kCZS4lUPH1Or79iyVnPUX94bSnlE&start=false&loop=false&delayms=15000).
  * This has been consuming most of my time.
  * It's done, and I spent too much time on it!
* Did the exercises in 4.3 again, getting stuck on 4 and 5. 4 currently "works" but not as intended. The issue I'm struggling with is incorporating circumference. Did some tests with circumference = math.pi * (r * 2) but the correct approach is not yet apparent.

### In-class ###
* I need to install [Swampy](http://allendowney.com/swampy/install.html).
* Best practice: Use docstrings!
* It is possible to define a global variable inside a local function that can be accessed outside the function.
  * To use: call global as a reserved function with variable as argument
* Glossary: *None* is a sentinel value, can reliably return "nothing"
* Overload on surrounding quotation marks to pass a string with quotes inside.
* Local variables need to have a default value.
* Glossary: *Dereference* refers to contents of a variable.
* Best practice: Don't use global variables!
  * Demonstration: scope.py
  * Best practice: Don't use local and global variable names that are the same or single-letter
* Jeff wants us to practice importing modules such as *string

## Week 1 ##
### Homework & Reading ###
* Ch1: Had issues with 1_3 due to lack of help library on Windows IDLE
* Ch2: Can't remember how to concatenate a string and an integer/float
  * Resolved: In Chapter 3 I figured out just to convert to strings
* Ch3: I don't understand the purpose of printing() a function
  * Hypothesis: Does it show the memory address of the function?
* Ch3: I don't understand why the flow of execution can be "violated" in 3_2
  * Week2: Initially misinterpreted this, mistakenly thought a function was called before it was defined, oops!
* 3_2: Can't get the len() of an integer, not sure how to handle exception without knowledge of conditional statements
* 3_4: The wording really confused me. Working backwards from the provided solution helped immensely.
* 3_5: At first I didn't realize that separating print() values with commas would create an extra space, but my grid still showed up intact, albeit spaced apart. Corrected this but ended up dropping some multiplication to '- ' dashes followed by spaces.
  * Corrected the extra spacing issue in 3_5_2 but left it intact on the simpler 3_5_1 to demonstrate my original thought process.
