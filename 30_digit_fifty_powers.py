def digit_fifth():
	answer = 0
	for i in range(2,354295):
		total = 0
		temp = i
		while i!=0:
			total = total + (i%10)**5
			print(total,i)
			i = i//10
			# print("value of i is:",i)

		if total == temp:
			answer = answer + temp

	return answer

print(digit_fifth())

