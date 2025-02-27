import numpy as np

def submatrix_with_n_numbers(matrix, n=46):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    if np.all(matrix[i:k + 1, j:l + 1] == 46):
                        count += 1
    return count