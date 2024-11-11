def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	c = []
	
	if len(a[0]) != len(b):
		return -1
	
	for row in a:
		dot_product = sum(x * y for x, y in zip(row, b))
		c.append(dot_product)
	
	return c