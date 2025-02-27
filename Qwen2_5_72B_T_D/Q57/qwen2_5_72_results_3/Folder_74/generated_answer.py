import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_generate(matrix, start_row, start_col, end_row, end_col):
        return matrix[start_row:end_row, start_col:end_col]
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    sub = submatrix_generate(matrix, start_row, start_col, end_row, end_col)
                    if np.sum(sub) == 88:
                        result.append(sub)
    return result