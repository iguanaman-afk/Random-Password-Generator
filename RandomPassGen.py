import random

file = open('allpsswrds.txt', 'a')

email = input("What email did you use?")
uname = input("What username did you use?")
account = input("What is this for?")

gen_psswrd = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

list_of_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
                '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
ugly_pass = random.sample(list_of_char, len(gen_psswrd))

real_pass = (''.join(ugly_pass))

keys = "email: "+str(email)+" | uname: "+str(uname)+" | account: "+str(account)+" | password: "+str(real_pass)

print("Here is the key for " + account)
print(keys)

file.write('\n')
file.write(keys)
file.close()
