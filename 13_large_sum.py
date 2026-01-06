numbers = []

n = int(input())
for _ in range(n):
    numbers.append(input())


def large_sum():
	carry = 0
	answer = ''
	for i in range(49,-1,-1):
		total = 0
		for j in range(100):
			temp = numbers[j]
			total = total + int(temp[i])
		
		total = int(total+carry)
		answer = str(int(total%10)) + answer
		print(total,answer)
		carry = int(total//10)

	answer = str(carry)+answer

	return int(answer)

print(large_sum())