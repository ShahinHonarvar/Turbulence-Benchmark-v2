import numpy as np

def submatrix_with_n_numbers(matrix, n=90):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.prod(submatrix.shape) == n * n:
                    count += 1
    return count