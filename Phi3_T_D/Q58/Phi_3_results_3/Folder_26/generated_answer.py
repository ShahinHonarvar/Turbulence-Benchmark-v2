import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 115
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows:
                for k in range(j, j + n):
                    if k + n <= cols:
                        submatrix = matrix[i:i + n, k:k + n]
                        if np.all(submatrix == n * np.ones((n, n))):
                            count += 1
    return count