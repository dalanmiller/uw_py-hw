from find import find

# Test queries
print 'Please refer to comments for explanation.'
print find('abcdefghijk', 'd', 3)	# d is found after position 3
print find('abcdefghijk', 'd', 4)	# d is not found after position 4
print find('abcdefghijk', 'n', 0)	# n is not found after beginning
