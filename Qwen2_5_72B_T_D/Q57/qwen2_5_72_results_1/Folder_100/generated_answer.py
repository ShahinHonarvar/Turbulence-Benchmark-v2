import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(matrix, target_sum):
        row_len, col_len = matrix.shape
        submatrices = []
        for start_row in range(row_len):
            for end_row in range(start_row, row_len):
                for start_col in range(col_len):
                    for end_col in range(start_col, col_len):
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices_with_sum(matrix, 28)