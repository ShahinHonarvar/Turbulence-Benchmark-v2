import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 80
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            if matrix[i:i + n, j:j + n].size == n:
                count += 1
    return count