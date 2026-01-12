def amicable_pair():
	answer = 0
	dictionary = {}
	stack = set()
	for i in range(1,10001):		
		total = find_divisor_total(i)
		dictionary[i] = total
		if total == i:
			continue
		if total in dictionary.keys():
			if dictionary[total] == i:
				# answer = answer + i
				print(i,total)
				stack.add(total)
		else:
			next_total = find_divisor_total(total)
			dictionary[total] = next_total
			if dictionary[total] == i:
					# answer = answer + total
					stack.add(total)
					# stack.add(i)

	print(stack)
	for i in stack:
		answer = answer + i
	return answer


def find_divisor_total(num):
	total = 0
	for j in range(1,num):
		if num%j ==0:
			total = total + j

	return total

# print(find_divisor_total(6))
print(amicable_pair())
# print(find_divisor_total(28))
