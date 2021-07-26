
'''
####### WARNING #######

THIS CODE IS REALLY INEFFICIENT, DON'T EVER USE IT !!!! THIS WAS A LAZY-WORK
IN BIG O NOTATION, THAT'D BE N*N

ONCE AGAIN, DON'T EVER USE IT !!!!

BUT I'LL FIX IT WHEN I DO PROJECT EULER IN R

'''


def smallest_possible():
	n = 100
	counter = 0
	while True:
		for i in range(1,21):
			if n % i == 0:
				counter += 1
		if  counter == 20:
			return n
			
		else:
			counter = 0
			n += 10

if __name__ == '__main__':
	print(smallest_possible())
