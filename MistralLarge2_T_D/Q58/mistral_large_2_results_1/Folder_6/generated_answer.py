import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    if (x - i + 1) * (y - j + 1) == 122:
                        count += 1
    return count