import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(i + 1, n):
                for l in range(j + 1, n):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 118:
                        count += 1
    return count