import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            if i + 12 < n and j + 12 < n:
                submatrix = matrix[i:i + 13, j:j + 13]
                if np.equal(submatrix, 139).all():
                    count += 1
    return count