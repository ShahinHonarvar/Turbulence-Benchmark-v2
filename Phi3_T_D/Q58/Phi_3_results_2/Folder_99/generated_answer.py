import numpy as np

def submatrix_with_n_numbers(matrix):
    count, n = (0, 146)
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + n <= rows:
                if j + n <= cols:
                    submatrix = matrix[i:i + n, j:j + n]
                    if np.sum(submatrix) == n:
                        count += 1
    return count