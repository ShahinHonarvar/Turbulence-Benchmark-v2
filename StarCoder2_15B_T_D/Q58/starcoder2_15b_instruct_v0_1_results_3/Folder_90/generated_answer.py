import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 176
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if sub_matrix.size == n:
                count += 1
    return count