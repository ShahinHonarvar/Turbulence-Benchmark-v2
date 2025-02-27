import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(mat, start_row, start_col, end_row, end_col):
        submat = mat[start_row:end_row, start_col:end_col]
        return (submat, np.sum(submat))
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submat, subsum = sum_submatrix(matrix, start_row, start_col, end_row, end_col)
                    if subsum == -83:
                        result.append(submat)
    return result