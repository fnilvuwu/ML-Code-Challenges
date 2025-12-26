def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
# Return a list where each element is the dot product of a row of 'a' with 'b'.
# If the number of columns in 'a' does not match the length of 'b', return -1.
	length_a = len(a)
	width_a = len(a[0])

	width_b = len(b)

	if width_a != width_b:
		return -1

	result = []
	for i in range(length_a):
		dot = 0
		for j in range(width_b):
			dot += a[i][j] * b[j]

		result.append(dot)

	return result


print(matrix_dot_vector([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))
print(matrix_dot_vector([[1, 2], [2, 4], [6, 8], [12, 4]], [1, 2, 3]))
print(matrix_dot_vector([[1.5, 2.5], [3.0, 4.0]], [2, 1]))
print(matrix_dot_vector([[1]], [5]))
print(matrix_dot_vector([[1, 2, 3, 4, 5]], [1, 1, 1, 1, 1]))
print(matrix_dot_vector([[0, 0], [0, 0], [0, 0]], [5, 3]))
print(matrix_dot_vector([[-1, -2], [-3, -4]], [1, 1]))
print(matrix_dot_vector([[2]], [0]))