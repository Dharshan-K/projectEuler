def digit_factorial():
	answer = 0
	for i in range(3,1000001):
		temp4 = i
		temp = 0
		temp2 = 0
		while temp4 > 0:
			temp = temp4%10
			temp1 = 1
			for j in range(1,temp+1):
				temp1 = temp1 * j

			temp2 = temp2 + temp1
			temp4= temp4 //10

		if temp2 == i:
			print(i)
			answer = answer + i


	return answer

print(digit_factorial())