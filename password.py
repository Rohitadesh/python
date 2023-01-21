import random

def password_genrator(password):
	small_letter='abcdefghijklmnopqrstuvwxyz'
	capital_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	digits='0123456789'
	special="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~."
	length=6
	ans=small_letter+capital_letter+digits+special
	password=''.join(random.sample(ans,length))
	return password
password=''
print(password_genrator(password))

