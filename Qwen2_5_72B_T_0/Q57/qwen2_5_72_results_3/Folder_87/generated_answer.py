import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submat = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submat) == target_sum:
                            result.append(submat)
        return result
    return submatrix_sum(matrix, 35)