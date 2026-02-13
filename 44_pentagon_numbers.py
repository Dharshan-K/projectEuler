def find_pentagon_numbers():
	arr = []
	answer = []
	answer2 = set()
	for i in range(1,3000):
		temp = (i*(i*3 - 1))//2
		arr.append(temp)
		answer2.add(temp)


	for i in range(0,len(arr)):
		for j in range(i+1,len(arr)):
			temp1 = arr[i]+arr[j]
			temp2 = arr[j] - arr[i]
			# print(temp1, temp2)
			if temp1 in answer2 and temp2 in answer2:
				answer.append(temp2)

	answer.sort()
	print(answer)
	return answer[0]

find_pentagon_numbers()

