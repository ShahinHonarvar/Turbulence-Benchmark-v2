import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        yield matrix[start_row:end_row + 1, start_col:end_col + 1]
    rows, cols = matrix.shape
    result = []
    for submatrix in submatrices(matrix, rows, cols):
        if np.sum(submatrix) == 411:
            result.append(submatrix)
    return result