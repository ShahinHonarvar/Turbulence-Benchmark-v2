import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0

    def count_submatrix(i, j):
        for r in range(i, m):
            for c in range(j, n):
                if (r - i + 1) * (c - j + 1) == 130:
                    count.append(1)
    for i in range(m):
        for j in range(n):
            count_submatrix(i, j)
    return len(count)