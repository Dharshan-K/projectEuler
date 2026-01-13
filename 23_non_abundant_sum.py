def non_abundant_sum():
	stack = [] # array of abundant numbers
	for i in range(12,28123):
		if find_divisor_total(i):
			stack.append(i)

	sec_stack = [False] * 29000
	for j in range(len(stack)):
		for k in range(j, len(stack)):
			s = stack[j] + stack[k]
			if s<=28123:
				sec_stack[s] = True
			else:
				break

	total = 0
	count = 0
	for i in range(1,28123+1):
		if sec_stack[i] == False:
			total = total + i

	return total




def find_divisor_total(num):
	total = 0
	for j in range(1,num):
		if num%j ==0:
			total = total + j

	if total > num:
		return True
	else:
		return False


print(non_abundant_sum())