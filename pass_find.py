

password = input('Input password to find. ')



with open('c:/Users/nick/wordlists.lst', 'r') as wordlist:
	for line in wordlist:
		print(line + '\n')
		if line == password:
			print("[+] Password Found: " + password)
			break
		else:
			continue