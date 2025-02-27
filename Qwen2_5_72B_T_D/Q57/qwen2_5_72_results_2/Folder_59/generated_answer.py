import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target):
        m, n = mat.shape
        result = []
        for start_row in range(m):
            for start_col in range(n):
                for end_row in range(start_row + 1, m + 1):
                    for end_col in range(start_col + 1, n + 1):
                        if np.sum(mat[start_row:end_row, start_col:end_col]) == target:
                            result.append(mat[start_row:end_row, start_col:end_col])
        return result
    return submatrix_sum(matrix, 2)