def pythogorean_product():
	for i in range(1,1000):
		for j in range(1,1000):
			if i+j > 1000:
				break
			for k in range(1,1000):
				if i+j+k > 1000:
					break
				elif i+j+k == 1000:
					temp = i*i + j*j;
					if temp == k*k:
						print(i,j,k)
						return i*j*k 


print(pythogorean_product())