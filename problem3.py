 # Solution to Problem 1 - Multiples 3 and 5
# - GabrielSilvaSouza
#
# Explore more on: 
# https://github.com/GabrielSilvaSouza/Project-Euler-in-Python
# 

def find_prime(number):
	i = 0   
	n = 1	#First divisor
	prime_storage = []   #list of prime numbers
	while i != 1:   #structure that will allow us to find the sucessives divisor and primers
		if number % n == 0:
			prime_storage.append(n)
			number = number/n
		elif number == 1:   #break the look
			return prime_storage[len(prime_storage)-1]
		n += 1	

if __name__ == '__main__':
	print(find_prime(600851475143))
