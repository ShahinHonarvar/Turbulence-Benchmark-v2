import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a two-dimensional numpy matrix of integers')
    n, m = matrix.shape
    count = 0
    for i in range(n):
        for j in range(m):
            for size in range(1, min(n - i, m - j) + 1):
                if (matrix[i:i + size, j:j + size] == 107).all():
                    count += 1
    return count