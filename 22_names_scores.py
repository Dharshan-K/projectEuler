with open("0022_names.txt","r") as file:
	content = file.read()

names = content.replace('"','').split(',')

print(names[938])
names.sort()
print(names[938])

# print(names)

total = 0
count = 1
for words in names:
	temp = 0
	for j in range(len(words)):
		temp = temp + (ord(words[j]) - ord('A') + 1)

	total = total + (temp * count)
	print(words, total, temp, count)
	count = count + 1

print(total)

