import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if matrix.ndim != 2:
        raise ValueError('Input must be a 2D matrix')
    R, C = matrix.shape
    result = []

    def check_sum(sub_matrix):
        return np.sum(sub_matrix) == -59

    def find_submatrices(i, j, current):
        if i < R and j >= 0:
            if check_sum(current):
                result.append(current)
            find_submatrices(i + 1, j, np.vstack((current, matrix[i])))
            find_submatrices(i, j - 1, current[:, :-1])
            find_submatrices(i + 1, j - 1, np.vstack((current, matrix[i])))
    for i in range(R):
        find_submatrices(i, C - 1, matrix[i])
    return result