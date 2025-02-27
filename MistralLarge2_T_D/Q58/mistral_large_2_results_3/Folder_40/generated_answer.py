import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i, j] == 1:
                for k in range(i, m):
                    for l in range(j, n):
                        if np.sum(matrix[i:k + 1, j:l + 1]) == (k - i + 1) * (l - j + 1):
                            count += 1
    return count