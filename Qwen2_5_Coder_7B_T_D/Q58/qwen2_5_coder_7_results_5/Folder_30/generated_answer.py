import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 94
    for i in range(rows):
        for j in range(cols):
            if i + 9 <= rows and j + 9 <= cols:
                submatrix = matrix[i:i + 9, j:j + 9]
                if np.sum(submatrix) == n:
                    count += 1
    return count