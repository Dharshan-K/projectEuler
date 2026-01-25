def distinct_powers():
	dictionary = set()

	for i in range(2,101):
		for j in range(2,101):
			dictionary.add(i**j)

	return len(dictionary)

print(distinct_powers())