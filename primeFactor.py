import math;

def primeFactor(num):
	numbers = []
	factors = findFactors(num);
	for number in factors:
		factorNumber = 2;
		root = math.sqrt(number)
		isPrime = True;
		while factorNumber <= root:
			if number%factorNumber == 0:
				isPrime = False
			factorNumber = factorNumber+1;
		if isPrime:
			numbers.append(number)
	print(numbers)
	return numbers



def findFactors(num):
	factors = []
	factorNumber = 1
	root = math.sqrt(num)
	while factorNumber <= root:
		if num%factorNumber == 0:
			factors.append(factorNumber)
			factors.append(num/factorNumber)
		
		factorNumber = factorNumber + 1;

	print(factors)
	return factors;


primeFactor(600851475143)



