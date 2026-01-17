
def permutations(arr):
	count = 0

	def backtrack(start, result, count, arr2):

		if start == len(arr):
			count = count + 1
			result.append(arr.copy())
			print(count, arr)
			if count == 1000000:
				arr2.append(arr.copy())
			return

		for i in range(start, len(arr)):
			arr[start], arr[i] = arr[i], arr[start]

			backtrack(start+1, result, count, arr2)

			arr[start],arr[i] = arr[i], arr[start]

	result = []
	
	answer1 = []
	backtrack(0, result, count, answer1)
	print(answer1)
	return result


arr = [0,1,2,3,4,5,6,7,8,9]
answer = permutations(arr)
print(answer[1000000])
# print(answer1)