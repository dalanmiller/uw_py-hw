def uses_only(root_string, query):
	"Evaluates as True if each query letter is found in root string"
	letter_matches = 0
	for qletter in query:
		# index_matches = False
		# for rletter in root_string:
		# 	if rletter == qletter:
		# 		index_matches = True
		# if index_matches:
		# 	letter_matches += 1

		# String .find method returns the location of the substring if
		# found, otherwise it returns -1. So we know if the result is not
		# -1 then qletter exists in root_string and can thus increment
		# letter_matches.

		# No need to iterate through each letter of the
		# query and then iterate through each letter
		# of the root string on top of that. This way has max operations
		# of the length of the query versus your way which has max
		# operations of query length multiplied by length of
		# the root_string. FOR LOOP ALL THE THINGS!

		#http://docs.python.org/2/library/string.html#string.find

		if root_string.find(qletter) != -1:
			letter_matches += 1

	return len(query) == letter_matches

print uses_only('andreas', 'ed')

print uses_only('monkeyman', 'am')

print uses_only('in reptar we trust', 'ep')

print uses_only('zombie nation', 'q')
