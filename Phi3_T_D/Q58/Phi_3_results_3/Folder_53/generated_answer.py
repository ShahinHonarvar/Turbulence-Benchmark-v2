import numpy as np

def submatrix_with_n_numbers(matrix):
    M, N = matrix.shape
    count = 0
    for i in range(M):
        for j in range(N):
            for k in range(i, M):
                for l in range(j, N):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 24:
                        count += 1
    return count