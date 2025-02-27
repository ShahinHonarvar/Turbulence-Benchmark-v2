import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    target_size = 120
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == target_size:
                        count += 1
    return count