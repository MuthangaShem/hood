alph = '0abcdefghijklmnopqrstuvwxyz'
sentence = 'bad ok'
words = sentence.split(' ')
counter = len(words)
print(counter)
print(words)
for word in words[0]:
	for letter in word:
		print(letter)
		# for beta in letter:
		# 	counter += alph.index(beta)
		# 	print(counter)



letters = list(words)
# for letter in letters:
# 	counter += alph.index(letter)
# print(counter)