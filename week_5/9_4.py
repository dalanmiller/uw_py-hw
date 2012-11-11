def uses_only(root_string, query):
	"Evaluates as True if each query letter is found in root string"
	letter_matches = 0
	for qletter in query:
		index_matches = False
		for rletter in root_string:
			if rletter == qletter:
				index_matches = True
		if index_matches:
			letter_matches += 1
	return len(query) == letter_matches

print uses_only('andreas', 'ed')
