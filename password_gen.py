import itertools

wordlist = open('c:/Users/nick/wordlists.lst', 'a')

temp = []
num = '1234567890'

min_len = input("Min. password length. ")
max_len = input("Max. password length. ")
keyinput = input("Enter keywords(seperated by commas). ")

keywords = ''.join(keyinput.split(',')) + ''.join(keyinput.split(',')).upper() + num

for i in range(int(min_len), int(max_len)):
	comb = itertools.combinations(keywords, i)
	
	for comb_iter in comb:
		temp += comb_iter
		
	wordlist.write(''.join(map(str, temp)))
	
wordlist.close()
		
		
		
		
