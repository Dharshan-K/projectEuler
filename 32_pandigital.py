def pandigital():
	n = 1
	dictionary = set()
	for i in range(1,10):
		for j in range(1000,10000 // i):
			k = i * j
			if findPandigital(i,j,k):
				dictionary.add(k)

	for i in range(10,100):
		for j in range(100, 1000):
			k = i*j
			if findPandigital(i,j,k):
				dictionary.add(k)

	answer = 0
	for i in dictionary:
		answer = answer + i

	print(dictionary)
	return answer





def findPandigital(i,j,k):
	temp = str(i) + str(j) + str(k)

	if len(temp) == 9 and "".join(sorted(temp)) == '123456789':
		return True
	return False
	

print(pandigital())