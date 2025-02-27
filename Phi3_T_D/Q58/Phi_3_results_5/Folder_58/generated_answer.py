import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    if m == 0 or n == 0:
        return 0
    submatrices = []
    for i in range(m):
        for j in range(n):
            for size_m in range(i + 1, m + 1):
                for size_n in range(j + 1, n + 1):
                    if (size_m - i) * (size_n - j) == 185:
                        submatrices.append(matrix[i:size_m, j:size_n])
    return len(submatrices)