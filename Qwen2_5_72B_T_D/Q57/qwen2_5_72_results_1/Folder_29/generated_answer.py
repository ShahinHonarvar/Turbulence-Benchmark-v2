import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(i, j, current_sum, current_submatrix, result):
        if current_sum == 84:
            result.append(np.array(current_submatrix))
            return
        if i >= matrix.shape[0] or j >= matrix.shape[1]:
            return
        for ni, nj in [(i, j + 1), (i + 1, j)]:
            if 0 <= ni < matrix.shape[0] and 0 <= nj < matrix.shape[1]:
                find_submatrices(ni, nj, current_sum + matrix[ni, nj], current_submatrix + [matrix[ni, nj]], result)
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            find_submatrices(i, j, matrix[i, j], [matrix[i, j]], result)
    return [np.array(r).reshape(-1, 1) for r in result if np.sum(r) == 84]