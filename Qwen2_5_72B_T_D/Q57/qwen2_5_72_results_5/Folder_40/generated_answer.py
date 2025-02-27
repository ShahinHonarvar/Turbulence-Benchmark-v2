import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(mat, target_sum):
        row_len, col_len = mat.shape
        result = []
        for start_row in range(row_len):
            for start_col in range(col_len):
                for end_row in range(start_row + 1, row_len + 1):
                    for end_col in range(start_col + 1, col_len + 1):
                        sub_matrix = mat[start_row:end_row, start_col:end_col]
                        if np.sum(sub_matrix) == target_sum:
                            result.append(sub_matrix.tolist())
        return result
    return find_submatrices(matrix, -10)