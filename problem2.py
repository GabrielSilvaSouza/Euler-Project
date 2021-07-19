 # Solution to Problem 1 - Multiples 3 and 5
# - GabrielSilvaSouza
#
# Explore more on: 
# https://github.com/GabrielSilvaSouza/Project-Euler-in-Python 

def sum_of_even():
	counter = 2   #Setting the first even
	temp = [1,2]  #Setting the list that will be use as base to counting
	i = 0  #while's counter
	while i < 4000000:
		i = temp[0] + temp[1]   #receive the two elements from the "temp" list
		if i % 2 == 0:   #check if it's even
			counter += i
		temp.append(i)   #change the elements to the next counting
		temp.pop(0)
		
	return counter
	
if __name__ == '__main__':
	print(sum_of_even())
		

