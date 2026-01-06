def largest_collatz():
	maximum = 0
	value = 0
	for i in range(0,1000000):
		count = 1
		temp = i
		while temp>1:
			if temp%2 == 0:
				temp = temp/2
			else:
				temp = (3*temp)+1

			count = count + 1
		print(i,count)
		
		if count > maximum:
			value = i
			maximum = count
			# print(value,maximum)


	return value

print(largest_collatz())

