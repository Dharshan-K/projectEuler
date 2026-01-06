# def sum_of_squares(num):
# 	temp = 1
# 	total = 0
# 	count = 1
# 	while count <= num:
# 		if count%2 != 0:
# 			total = total + (count*count)
# 			print(count)

# 		count = count+1


# 	return total

def sum_of_odd_squares(num):
    total = 0
    # Start at 1, go up to num, step by 2 to get only odd numbers
    for i in range(1, num + 1, 2):
        total += i * i
    return total
print(sum_of_odd_squares(332000))




