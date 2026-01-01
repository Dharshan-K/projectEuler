import math
def two_million_prime_sum():
	n=2;
	prime = 0;
	count = 0
	total = 0
	while n < 2000001:
		square = int(math.sqrt(n));
		for i in range(2, square+1):
			if n % i ==0:
				break
		else:
			count = count+1
			prime = n
			total = total + n

		n=n+1

	return total


print(two_million_prime_sum())

