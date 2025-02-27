import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix of integers.')
    m, n = matrix.shape
    target_sum = -185
    submatrices = []
    for size in range(1, min(m, n) + 1):
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                sub_matrix = matrix[i:i + size, j:j + size]
                if np.sum(sub_matrix) == target_sum:
                    submatrices.append(sub_matrix)
    return submatrices