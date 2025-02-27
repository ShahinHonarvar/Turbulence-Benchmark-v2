import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, sum_value):
        submatrices = []
        for start_row in range(row + 1):
            for start_col in range(col + 1):
                for end_row in range(start_row, row + 1):
                    for end_col in range(start_col, col + 1):
                        if np.sum(matrix[start_row:end_row + 1, start_col:end_col + 1]) == sum_value:
                            submatrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1].tolist())
        return submatrices
    row, col = matrix.shape
    return find_submatrices(row, col, 93)