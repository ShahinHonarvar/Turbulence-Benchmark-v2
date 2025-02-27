import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        row_count, col_count = mat.shape
        submatrices = []
        for start_row in range(row_count):
            for end_row in range(start_row, row_count):
                for start_col in range(col_count):
                    for end_col in range(start_col, col_count):
                        current_submatrix = mat[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(current_submatrix) == target_sum:
                            submatrices.append(current_submatrix)
        return submatrices
    return find_submatrices_with_sum(np.array(matrix), 40)