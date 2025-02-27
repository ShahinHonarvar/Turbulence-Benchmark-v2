import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum):
        row_count, col_count = matrix.shape
        submatrices = []
        for start_row in range(row_count):
            for end_row in range(start_row, row_count):
                for start_col in range(col_count):
                    for end_col in range(start_col, col_count):
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        if np.sum(submatrix) == target_sum:
                            submatrices.append(submatrix)
        return submatrices
    return find_submatrices(matrix, -452)