import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 40
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                submatrix = matrix[i:i + n, j:j + n]
                if np.unique(submatrix).size == n:
                    count += 1
    return count