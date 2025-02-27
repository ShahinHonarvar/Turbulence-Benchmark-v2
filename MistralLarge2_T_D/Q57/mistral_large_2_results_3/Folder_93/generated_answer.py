import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start_row, start_col, end_row, end_col):
        if end_row < matrix.shape[0] and end_col < matrix.shape[1]:
            submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
            if np.sum(submatrix) == -65:
                result.append(submatrix)
            find_submatrices(start_row, start_col, end_row, end_col + 1)
            find_submatrices(start_row, start_col, end_row + 1, end_col)
        if end_col < matrix.shape[1]:
            find_submatrices(start_row, start_col, end_row, end_col + 1)
        if end_row < matrix.shape[0]:
            find_submatrices(start_row, start_col, end_row + 1, end_col)
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            find_submatrices(i, j, i, j)
    return result