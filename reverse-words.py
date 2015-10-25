# Reverse words in a string by putting all the words on a stack, and printing them in the order they are popped

def reverse_words(str):
	nstring = " "
	words = []
	length = len(str)
	index = 0
	while index < length:
		if(str[index] != ' '):
			start = index
			while index < length and str[index] != ' ':
				index += 1
			words.append(str[start:index])
		index += 1
		
	while len(words) > 0:
		nstring = nstring + words.pop() + ' ' 
	return nstring

print(reverse_words("Today my hair is beautiful."))

