def lattice_path(x,y):
	print(x,y)
	if x==5 and y==5:
		return 1

	if y<5:
		return lattice_path(x,y+1)

	if x<5:
		return lattice_path(x+1,y)

	return lattice_path(x+1,y) + lattice_path(x,y+1)


print(lattice_path(1,1))