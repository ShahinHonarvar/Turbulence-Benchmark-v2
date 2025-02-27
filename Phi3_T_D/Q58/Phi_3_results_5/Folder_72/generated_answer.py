import numpy as np

def submatrix_with_n_numbers(matrix):
    n = len(matrix)
    m = len(matrix[0]) if n > 0 else 0
    count = 0
    for i in range(n):
        for j in range(m):
            for k in range(i + 3, n + 1):
                for l in range(j + 3, m + 1):
                    if np.all(matrix[i:k, j:l]):
                        count += 1
    return count