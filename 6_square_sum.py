def square_sum():
	square_sum = 0
	total_sum = 0
	for i in range(1,101):
		total_sum = total_sum + i;
		square_sum = square_sum + (i*i)
	total_sum = total_sum*total_sum

	return total_sum-square_sum


print(square_sum())