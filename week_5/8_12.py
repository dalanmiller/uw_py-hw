def rotate_word(s, n):
	for letter in s:
		encoded_letter = ord(letter) + n
		decoded_letter = chr(encoded_letter)
		print decoded_letter,
	print '\r'

rotate_word('cheer', 7)
rotate_word('melon', -10)
