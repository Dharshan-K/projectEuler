def reciprocal_cycles():
	maximum = 0
	answer = 0
	answer1 = 0
	for i in range(2,1001):
		temp = 1/i
		temp = str(temp)
		temp = temp.replace(".", '')
		
		
		answer = find_recurring_cycle(temp[1:])
		print(i,temp[1:],answer)
		if answer > maximum:
			maximum = answer
			answer1 = i

	return answer1


def find_recurring_cycle(string):
	dictionary = {}
	for i in range(len(string)):
		# print(string[:i])
		if string[i] in dictionary:
			# print(string,i)
			return i + 1

		dictionary[string[i]] = 1
	# print(dictionary)
	return 0



print(reciprocal_cycles())