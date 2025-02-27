import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for row_beg in range(rows):
        for col_beg in range(cols):
            for row_end in range(row_beg, rows):
                for col_end in range(col_beg, cols):
                    submatrix = matrix[row_beg:row_end + 1, col_beg:col_end + 1]
                    if submatrix.sum() == -9:
                        submatrices.append(submatrix)
    return submatrices