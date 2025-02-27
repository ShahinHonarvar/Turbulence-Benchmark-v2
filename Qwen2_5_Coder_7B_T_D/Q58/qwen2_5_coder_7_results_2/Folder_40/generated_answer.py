import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.all(submatrix == 1):
                        count += 1
    return count