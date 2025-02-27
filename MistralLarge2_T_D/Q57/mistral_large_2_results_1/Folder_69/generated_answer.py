import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def find_submatrices(start_row, start_col):
        for row in range(start_row, rows):
            for col in range(start_col, cols):
                for sub_row in range(row + 1, rows + 1):
                    for sub_col in range(col + 1, cols + 1):
                        submatrix = matrix[row:sub_row, col:sub_col]
                        if submatrix.sum() == 752:
                            submatrices.append(submatrix.tolist())
    find_submatrices(0, 0)
    return submatrices