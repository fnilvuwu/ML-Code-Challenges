def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
	"""
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
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
