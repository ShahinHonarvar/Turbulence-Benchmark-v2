import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 56:
                if i + 1 < n:
                    for k in range(i + 1, n):
                        if matrix[k][j] == 56:
                            if j + 1 < m:
                                for l in range(j + 1, m):
                                    if matrix[i][l] == 56 and matrix[k][l] == 56:
                                        count += 1
    return count