# 
# Solution to Problem 4 - Largest palindrome product
# - GabrielSilvaSouza
#
# 
# https://github.com/GabrielSilvaSouza/Project-Euler-in-Python
# 

if __name__ == '__main__':
	l = []
	for i in range(999, 100,-1):
		for j in range(999, 100,-1):
			res = i*j
			if str(res) == str(res)[::-1]:
				l.append(res)
	l.sort(reverse=True)		
	print(l[0])
			
