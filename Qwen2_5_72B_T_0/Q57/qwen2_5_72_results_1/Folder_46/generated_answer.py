import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row_count, col_count = mat.shape
        result = []
        for start_row in range(row_count):
            for start_col in range(col_count):
                for end_row in range(start_row + 1, row_count + 1):
                    for end_col in range(start_col + 1, col_count + 1):
                        submatrix = mat[start_row:end_row, start_col:end_col]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, 416)