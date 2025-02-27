import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a 2D numpy matrix')

    def all_submatrices(mat, rows, cols):
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        yield mat[i:k, j:l]
    rows, cols = matrix.shape
    result = []
    for submatrix in all_submatrices(matrix, rows, cols):
        if submatrix.sum() == -46:
            result.append(submatrix)
    return result