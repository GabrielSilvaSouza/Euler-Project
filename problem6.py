def sum_of_squares(num):
	total = (num*(num+1)*(2*num + 1))/6
	return total

def square_of_sum(num):
	first = num - (num - 1)
	total = ((first + num)*num)/2
	return total*total

if __name__ == '__main__':
	print(int(square_of_sum(100) - sum_of_squares(100))) 

