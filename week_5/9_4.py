def uses_only (word, string):
	"9_4"
	for c in word:
		if c not in string:
			return False
	return True

# Unit test
print uses_only('mississipi', 'mississipi')
print uses_only('mississipi', 'oklahoma')
