def palindrome(num):
	reverseNumber = 0;
	num1 = num
	while num1 > 0:
		reminder = num1 % 10;
		reverseNumber = reverseNumber * 10 + reminder;
		num1 = num1 // 10;

	if reverseNumber == num:
		return True
	else:
		return False


def largestPalindrome(num):
	answer = 0
	for i in range(100,1000):
		for j in range(100,1000):
			temp = i*j
			if palindrome(temp) == True and temp > answer:
				answer = temp

	return answer


	


print(largestPalindrome(9009))