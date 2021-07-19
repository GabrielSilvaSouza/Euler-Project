counter = 1
temp = [1,2]
i = 0
while i < 4*(10**6):
	i = temp[0] + temp[1]	
	if i % 2 == 0:
		counter += i
	temp.append(i)
	temp.pop(0)
	print(temp,i)
	if i > 4*(10**6):
		print("rUNNED HERE")
		break
	

print(counter)
		

