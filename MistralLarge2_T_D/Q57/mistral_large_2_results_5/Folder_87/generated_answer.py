import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col):
        for row in range(start_row, rows):
            for col in range(start_col, cols):
                for end_row in range(row, rows):
                    for end_col in range(col, cols):
                        submatrix = matrix[row:end_row + 1, col:end_col + 1]
                        if np.sum(submatrix) == 35:
                            submatrices.append(submatrix)
    find_submatrices(0, 0)
    return submatrices