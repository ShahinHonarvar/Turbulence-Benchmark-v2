import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 107
    row, col = matrix.shape
    count = 0
    for i in range(row - n + 1):
        for j in range(col - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if sub_matrix.size == n:
                count += 1
    return count