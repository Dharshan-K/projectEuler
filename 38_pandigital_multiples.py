def pandigital_multiple():
	maximum = 0
	for i in range(1,1000000):
		string = ''
		for j in range(1,i+1):
			string = string + str(i*j)
			if len(string) == 9:
				if verify_pandigital(string):
					if int(string) > maximum:
						maximum = int(string)
			elif len(string) > 9:
				break

	return maximum

def verify_pandigital(string):
	if "".join(sorted(string)) == '123456789':
		return True
	return False

print(pandigital_multiple())