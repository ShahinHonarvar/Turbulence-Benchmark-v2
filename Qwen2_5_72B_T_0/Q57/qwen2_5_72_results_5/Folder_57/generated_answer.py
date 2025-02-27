import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row, col = mat.shape
        result = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                for start_col in range(col):
                    for end_col in range(start_col, col):
                        submat = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submat) == target_sum:
                            result.append(submat)
        return result
    return find_submatrices_with_sum(matrix, 13)