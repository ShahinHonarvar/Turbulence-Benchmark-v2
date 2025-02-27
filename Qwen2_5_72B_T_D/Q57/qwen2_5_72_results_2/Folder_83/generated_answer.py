import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        yield matrix[start_row:end_row + 1, start_col:end_col + 1]
    result = []
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    for submatrix in submatrices(matrix, rows, cols):
        if np.sum(submatrix) == -15:
            result.append(submatrix)
    return result