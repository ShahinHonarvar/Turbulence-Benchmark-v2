import numpy as np

def submatrix_with_n_numbers(matrix):
    result = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    count = np.count_nonzero(submatrix)
                    if count == 38:
                        result += 1
    return result