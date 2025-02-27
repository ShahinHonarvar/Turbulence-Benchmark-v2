import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(mat, target):
        row, col = mat.shape
        result = []
        for start_row in range(row):
            for start_col in range(col):
                for end_row in range(start_row + 1, row + 1):
                    for end_col in range(start_col + 1, col + 1):
                        sub = mat[start_row:end_row, start_col:end_col]
                        if np.sum(sub) == target:
                            result.append(sub.tolist())
        return result
    return find_submatrices(matrix, -13)