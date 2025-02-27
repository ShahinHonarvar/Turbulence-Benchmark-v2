import numpy as np

def generate_submatrices(matrix, row_start, col_start, row_limit, col_limit, target_sum, current_sum, row_count, submatrices):
    if row_count > 0 and current_sum == target_sum:
        submatrices.append(matrix[row_start:row_start + row_count, col_start:col_start + row_count])
    if (row_start > 0 or col_start > 0) and abs(current_sum - target_sum) < abs(current_sum):
        return
    for i in range(row_start, row_limit):
        for j in range(col_start, col_limit):
            row_sum = np.trace(matrix[i - row_count + 1:i + 1, j - row_count + 1:j + 1])
            generate_submatrices(matrix, i + 1, j + 1, row_limit, col_limit, target_sum, current_sum + row_sum, row_count, submatrices)

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n, m = matrix.shape
    for size in range(1, min(n, m) + 1):
        generate_submatrices(matrix, 0, 0, n, m, 64, 0, size, submatrices)
    return submatrices