import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 94
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                submatrix = matrix[i:i + n, j:j + n]
                count += 1 if submatrix.size == n * n else 0
    return count