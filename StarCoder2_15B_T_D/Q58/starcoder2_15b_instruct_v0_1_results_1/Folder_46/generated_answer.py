import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 13):
        for j in range(n - 11):
            sub_matrix = matrix[i:i + 14, j:j + 12]
            if sub_matrix.size == 144:
                count += 1
    return count