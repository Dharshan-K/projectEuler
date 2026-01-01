import math
def prime_number():
	n=2;
	prime = 0;
	count = 0
	while count < 10001:
		square = int(math.sqrt(n));
		for i in range(2, square+1):
			if n % i ==0:
				break
		else:
			count = count+1
			prime = n
			print(count,prime)

		n=n+1

	return prime


print(prime_number())

