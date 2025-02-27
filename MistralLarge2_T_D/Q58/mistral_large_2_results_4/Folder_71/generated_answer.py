import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for x in range(i + 1, m + 1):
                for y in range(j + 1, n + 1):
                    if np.prod((x - i, y - j)) == 78:
                        count += 1
    return count