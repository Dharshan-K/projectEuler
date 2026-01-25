def reciprocal_cycles():
	maximum = 0
	answer = 0
	for i in range(2,1001):
		remainder = 1%i
		dictionary = {}
		digits = []
		start = 0
		cycle = 0
		position = 0
		
		while remainder!=0:
			if remainder in dictionary:
				start = dictionary[remainder]
				cycle = digits[start:]
				if len(cycle) > maximum:
					maximum = len(cycle)
					answer = i
				break

			dictionary[remainder] = position
			remainder = remainder * 10
			digit = remainder // i
			digits.append(digit)
			remainder = remainder % i
			position =position+1			

	return answer

print(reciprocal_cycles())
# print(find_recurring_cycle("1098901098901099"))