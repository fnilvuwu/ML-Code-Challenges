def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
	result = []
	height = len(a)
	width = len(a[0])
	for i in range(width):
		row = []
		for j in range(height):
			row.append(a[j][i])
			if j == height - 1:
				result.append(row)
				
	return result

print(transpose_matrix([[1, 2], [3, 4], [5, 6]]))
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
print(transpose_matrix([[1, 2], [3, 4]]))
print(transpose_matrix([[1, 2, 3]]))
print(transpose_matrix([[1], [2], [3]]))
