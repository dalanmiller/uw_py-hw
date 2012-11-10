# Stassi's UW Python Homework #

**Developer:** Andreas Stassivik  
**Instructor:** Jeff Silverman  
**Class:** Certificate Program in Python Programming (2012)

* [Course Overview](https://docs.google.com/document/pub?id=1HHAean0DWMK_Wh1PbGcyd8VqFFWjI4d-o50lBAlILus)
* [Book](http://www.greenteapress.com/thinkpython/)
* [Book (Interactive)](http://interactivepython.org/courselib/static/thinkcspy/index.html)
* [Problems](http://www.commercialventvac.com/python/index.html)
* [Presentation: Andreas' Python Applications](https://docs.google.com/presentation/pub?id=1zAHdFjKlDOk62n0kCZS4lUPH1Or79iyVnPUX94bSnlE&start=false&loop=false&delayms=15000)

## Week 5 ##
### Homework & Reading ###
* Do homework in Ch. 10 & 12 (except 12_6)
* Finishing up 8, 9, 14 as well

#### Chapter 9 ####
* 9_2: I have learned much about words that abstain from containing the letter "e."
** Brought to you buy the letters D, A, N, I, E, L

#### Chapter 8 ####
* 8_10 brought me back to 6_6, which I dutifully executed. So glad I can do that crap in one line now.
* Finished Ch 8. 8_12 was a breeze until I tried perfecting my ouput to print on one line without whitespaces. Tried various methods used to trim spacing which did not work. A better solution might have been to output to a list and then print the join method, but I'm not quite there yet.
  * Also on 8_12, my cypher function is not iterating through the alphabet, but rather seems to be iterating through 255 ASCII character codes.

### In-class ###
* Checking in
* *pickling* or serializing is writing an object to file
* defining main() is a "way of making software reusable"
  * list test name = main passes
  * if software re-used, it won't execute
  * 14.9 explains in book
* pickle.HIGHEST_PROTOCOL is method that uses most recent version of pickle
* Jeff is a fan of temporary values due to easy of debugging
  * "Computer time is cheap and your time is valuable."
* 14_5 is an exercise to retrieve data from URL
* Lists are mutable and can be changed, unlike strings
* *in* is not as fast as hashing function since it searches a list from left to right
* Can't print a sort method because there's no output, it just rearranges things
  * sort*ed* does return something, confusingly enough...
* list .reverse method permanently reverses the order of list items
* .extend method is much faster than ++ operator for appending lists
* It's possible to define a range as +:- because you can count up to positive, then count backward from end or vice versa.
* Third range argument has special properties that allow you to skip items, print backwards, etc.
  * eg: ::-1 in brackets
* Careful not to copy a list wrong, remember to verify with x is y
* Tuples are immutable
  * This is why they are used!
  * Appending strings with a single comma is how to inject a string into a tuple rather than a list.
  * Although tuples can't be changed, the contained items can be changed!
* Variable arguments are functions that can have unlimited arguments passed to them, which creates tuples once values sent

## Week 4 ##
### Homework & Reading ###
* Due: 8, 9, 14 (*except* 14_7!)

#### Chapter 8 ####
* Self-reminder:
  * When writing an *or* conditional, it helps to visualize how each *or* segment would run independently of the others. This caused me a big headache on 8_2.
    * Thanks [Dan](https://github.com/dalanmiller)!
* Immutability:
  * Strings cannot be modified, but the effect of modifying them can be replicated by creating new strings that contain modifications.

#### Chapter 7 ####
* Catching up
* Self-reminders:
  * dir() function lists functions in module
  * pass is an argument(?) great for placeholders, does nothing

### In-class ###
* *assert* declares a statement is true, else throws AssertionError.
  * Will cover error handling in this week's homework
* Newton had to invent calculus in order to understand the solution to the in-class problem. This is an overt message that I should invent calculus.
* eval() evaluates problems
* Python 2 is default ASCII, Python 3 is default Unicode
  * unicode string syntax: u"string"
  * raw string syntax: r"string"
  * UTF8 most popular unicode
* Strings
  * Slices of strings are possible
  * Strings are *immutable*... but there are workarounds
    * Workaround: Convert strings to a list, always mutable!
* rstrip and lstrip can remove spaces at the start/end of strings
* You can print and modify recursion levels using sys module
* Tips for files:
  * Set multiple paths to variables, then change working directories using variables.
  * Use raw string inputs to bypass issues with tab, slash characters
* There are file-like objects that can be treated like files onced imported (eg: urls)
* Best practice: Handle exceptions
* Exceptions are objects, have their own class, and they can be user-defined
  * A module named exceptions exists, can be imported and output by dir()
* Exiting gracefully? Use sys.exit().
* *finally* block is apparently unconventional, but can be executed in addition to previous blocks
* Tell if an attribute of an object is a method via callable()
* Windows users have to treat file access in a unique way

## Week 3 ##
### Homework & Reading ###
* Due: 4, 5, 6, and 7

#### Chapter 6 ####
* Read through the chapter and did a few exercises. Struggled a bit with factorials (as I do with several mathematic concepts I'm rusty on) but I could follow the code examples.

#### Chapter 5 ####
* Created an HTML template for stack diagrams
* 5_2: Created my first recursive function
* 5_3: Built my first program with user input, utilizes conditional loops!
* 5_4: Getting the hang of programs with user input. Borrowed code from 5_3, went fast.

#### Chapter 4 ####
* After working on the initial exercises for a while and checking their answers, I am comfortable leaving Swampy and moving on to other exercises.
* Liked discovering the procedure for development plans:
  1. Write small program without function definitions
  1. Encapsulate program as function and name it
  1. Generalize function, add parameters
  1. Repeat prior steps, copypasta working code
  1. Refactor program's similar functions for efficiency

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
