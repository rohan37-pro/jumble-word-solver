import itertools
import os
import time
import string



with open(f"{os.getcwd()}/dictionary2.0.txt",'r') as file:
		words = file.readlines()

		words_lis = []
		for i in words:
			words_lis.append(i.lower().strip())

		alpha_range = {}
		found_char = 0
		alphabates = string.ascii_lowercase
		for i in alphabates:
			for j in words_lis:
				if j.startswith(f"{i}") and found_char == 0:
					alpha_range[i] = [words_lis.index(j)]
					found_char = 1
				elif not j.startswith(f'{i}') and found_char == 1:
					alpha_range[i].append(words_lis.index(j))
					found_char = 0

		alpha_range[i].append(None)
		#print(alpha_range)

message = """your computer might get hanged so
if you have 4 gb of ram :
	enter a jumble word lessthen or equal to 10 letters.
if you have 8 gb of ram :
	enter a jumble word lessthen or equal to 11 letters.
"""
print(message)

while True:
	jumble = input("enter a jubmle word : ")

	if jumble == "exit" or jumble=="quit":
		break

	lis = []
	a = itertools.permutations(jumble)
	for i in a :
		i = "".join(i)
		lis.append(i)


	start = time.time()
	for word in lis:
		word = word.lower()
		if word in words_lis[alpha_range[word[0]][0]:alpha_range[word[0]][1]]:
			print(f"{word} --> query ends in {time.time() - start} secs...")



	

