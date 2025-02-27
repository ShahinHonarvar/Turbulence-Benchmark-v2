import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submatrix = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, 411)