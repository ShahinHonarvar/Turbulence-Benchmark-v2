import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n, num):
        count = 0
        for i in range(m):
            for j in range(n):
                for k in range(i, m):
                    for l in range(j, n):
                        if (k - i + 1) * (l - j + 1) == num:
                            count += 1
        return count
    m, n = matrix.shape
    return count_submatrices(m, n, 131)