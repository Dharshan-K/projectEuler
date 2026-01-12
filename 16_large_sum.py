def large_sum():
	total = 1
	answer = 0
	for i in range(1,1001):
		total = total * 2

	print(total)
	while total > 0:
		answer = answer + (total%10)
		total = total//10

	return answer

	return answer
print(large_sum())
