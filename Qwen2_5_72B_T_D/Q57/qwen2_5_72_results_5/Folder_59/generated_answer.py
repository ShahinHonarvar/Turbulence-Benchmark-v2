import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(mat, target_sum):
        row_count, col_count = mat.shape
        submatrices = []
        for start_row in range(row_count):
            for end_row in range(start_row, row_count):
                for start_col in range(col_count):
                    for end_col in range(start_col, col_count):
                        submat = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submat) == target_sum:
                            submatrices.append(submat)
        return submatrices
    return submatrix_sum(matrix, 2)