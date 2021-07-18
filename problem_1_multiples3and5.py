# 
# Solution to Problem 1 - Multiples 3 and 5
# Copyright (c) . All rights reserved.
# 
#
# 

def sum_of_multiples(a):
	counter = 0
	while a > 0:
		if a % 5 == 0 or a % 3 == 0:
			counter += a
		a -= 1
	return counter
		
if __name__ == '__main__':
	number = int(input('Say a number, bro:\n'))
	number -= 1
	print(sum_of_multiples(number))

