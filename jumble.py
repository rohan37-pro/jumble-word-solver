import itertools
import os 

while True:
	jumble = input("enter a jubmle word : ")

	if jumble == "exit" or jumble=="quit":
		break

	lis = []
	a = itertools.permutations(jumble)
	for i in a :
		i = "".join(i)
		lis.append(i)

	with open(f"{os.getcwd()}/dictionary_words.txt",'r') as file:
		words = file.readlines()

		words_lis = []
		for i in words:
			words_lis.append(i.strip())

		for i in words_lis:
			if i.lower() in lis:
				print(i)
