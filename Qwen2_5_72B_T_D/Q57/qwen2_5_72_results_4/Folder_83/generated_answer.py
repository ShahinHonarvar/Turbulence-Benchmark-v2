import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, start_row, start_col, rows, cols):
        submatrices_list = []
        for end_row in range(start_row + 1, rows + 1):
            for end_col in range(start_col + 1, cols + 1):
                submatrices_list.append(matrix[start_row:end_row, start_col:end_col])
        return submatrices_list
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for submatrix in submatrices(matrix, start_row, start_col, rows, cols):
                if np.sum(submatrix) == -15:
                    result.append(submatrix)
    return result