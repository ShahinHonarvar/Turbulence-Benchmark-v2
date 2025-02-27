import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 5:
                if i + 1 < m:
                    if matrix[i + 1][j] == 5:
                        count += 1
                        if j + 1 < n and matrix[i][j + 1] == 5 and (matrix[i + 1][j + 1] == 5):
                            count += 1
    return count