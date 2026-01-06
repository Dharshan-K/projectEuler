def smallest_multiple():
	n=20
	while True:
		n=n+1
		for i in range(1,21):
			if n%i != 0:
				break
		else:
			return n

print(smallest_multiple())
