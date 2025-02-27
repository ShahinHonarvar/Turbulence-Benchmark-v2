import numpy as np

def get_submatrices(n, m):
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    result.append((i, j, k, l))
    return result

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    n, m = matrix.shape
    submatrices = get_submatrices(n, m)
    result = []
    for top_left, bottom_right in submatrices:
        current_submatrix = matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1]
        if current_submatrix.sum() == 17:
            result.append(current_submatrix)
    return result