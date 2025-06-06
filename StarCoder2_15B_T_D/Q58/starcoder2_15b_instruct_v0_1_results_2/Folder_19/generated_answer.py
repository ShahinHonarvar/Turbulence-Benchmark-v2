import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 17:
        return 0
    n = 17
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if sub_matrix.size == n:
                count += 1
    return count