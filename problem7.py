from sympy import *

def th_prime(p):
	counter = 0
	i = 0
	while True:
		i += 1
		if isprime(i) == True:
			counter += 1
		if counter == p:
			return i

if __name__ == '__main__':
	print(th_prime(10001))
