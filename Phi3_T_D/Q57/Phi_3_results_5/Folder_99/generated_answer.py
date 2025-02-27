import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    m, n = matrix.shape
    resulting_submatrices = []
    for size in range(1, min(m, n) + 1):
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.sum() == -185:
                    resulting_submatrices.append(submatrix)
    return resulting_submatrices