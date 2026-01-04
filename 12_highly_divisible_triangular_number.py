import math
def triangular_number():
	number_count = 1
	number_found = True
	current_number = 1
	natural_number = 0
	total = 0
	while number_found:
		divisor_count = 0
		natural_number = natural_number + 1
		total = natural_number + total
		root = int(math.sqrt(total))
		for i in range(1,root+1):
			if total%i == 0:
				divisor_count = divisor_count + 2

		if root * root == total:
			divisor_count = divisor_count - 1;

		print(total, divisor_count)
		if divisor_count >= 500:
			return total


print(triangular_number())