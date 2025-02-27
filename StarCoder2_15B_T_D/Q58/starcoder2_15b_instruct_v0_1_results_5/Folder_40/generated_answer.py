import numpy as np

def submatrix_with_n_numbers(matrix, n=1):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('The argument must be a two-dimensional numpy array.')
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == n:
                        count += 1
    return count