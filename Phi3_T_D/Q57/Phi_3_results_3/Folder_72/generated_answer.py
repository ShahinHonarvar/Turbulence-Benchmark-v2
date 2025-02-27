import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    results = []
    rows, cols = (matrix.shape[0], matrix.shape[1])
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if submatrix.sum() == 41:
                        results.append(submatrix)
    return results