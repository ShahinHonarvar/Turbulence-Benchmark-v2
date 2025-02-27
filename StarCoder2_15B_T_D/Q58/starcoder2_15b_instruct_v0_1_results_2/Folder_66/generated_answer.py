def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 1):
        for j in range(col - 1):
            sub_matrix = matrix[i:i + 2, j:j + 2]
            if sub_matrix.size == 42:
                count += 1
    return count