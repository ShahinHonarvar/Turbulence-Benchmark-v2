def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows - 2):
        for j in range(columns - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if sub_matrix.size == 78:
                count += 1
    return count