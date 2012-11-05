"Given that fruit is a string, what does fruit[:] mean?"

s = 'fruit'

print s
print type(s)

print '\r'

print s[:]
print type(s[:])

# Solution:
## string[:] returns a slice that begins at the beginning
## and ends at the end of the string.
