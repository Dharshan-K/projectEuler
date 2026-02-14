import math
def prime_number():
	n=2;
	prime = [];
	count = 0
	maximum = 0
	answer = 0
	dictionary = {}
	while count < 1000001:
		square = int(math.sqrt(n));
		for i in range(2, square+1):
			if n % i ==0:
				break
		else:
			prime.append(n)

		count = count+1

		n=n+1
	print(prime)

	arr2 = []
	temp = 0
	for i in range(0,len(prime)):
		temp = temp + prime[i]
		arr2.append(temp)

	print(arr2)

	for i in range(len(prime)):
		temp1 = 0
		for j in range(i + answer + 1,len(prime)):
			temp1 = arr2[j] - arr2[i]
			if temp1 >= 1000000:
				break			
			if temp1 in prime:
				if temp1 == 41:
					print(j,i,arr2[j] ,arr2[i])
				answer = j - i
				total = temp1

	print(total, answer)
	return total

print(prime_number())