import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(mat, row, col, path):
        if row == mat.shape[0] or col == mat.shape[1]:
            return [path] if np.sum(path) == 16 else []
        result = []
        for dr, dc in [(0, 1), (1, 0)]:
            result.extend(find_submatrices(mat, row + dr, col + dc, np.vstack((path, mat[row + dr, col + dc]))))
        return result
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result.extend(find_submatrices(matrix, i, j, np.array([[matrix[i, j]]])))
    return result