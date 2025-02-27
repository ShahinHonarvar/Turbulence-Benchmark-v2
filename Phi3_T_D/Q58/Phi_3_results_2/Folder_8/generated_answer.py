import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or not matrix.ndim == 2:
        return 0
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for xx in range(i, m):
                for yy in range(j, n):
                    submatrix = matrix[i:xx + 1, j:yy + 1]
                    if submatrix.size == 29:
                        count += 1
    return count