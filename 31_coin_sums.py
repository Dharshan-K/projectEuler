def coin_sums(total, index):
	coin_array = [200,100,50,20,10,5,2,1]

	if total == 200:
		return 1

	if total > 200 or index >= 8:
		return 0

	answer = coin_sums(total + coin_array[index], index) + coin_sums(total, index+1)

	return answer

print(coin_sums(0,0))