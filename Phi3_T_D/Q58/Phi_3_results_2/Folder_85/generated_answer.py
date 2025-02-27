import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    count = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            for size in range(1, min(n - i, m - j) + 1):
                if sum(matrix[i:i + size, j:j + size].flatten()) == 13:
                    count += 1
    return count