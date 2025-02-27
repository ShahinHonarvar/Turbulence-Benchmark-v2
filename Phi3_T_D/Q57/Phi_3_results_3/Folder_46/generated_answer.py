import numpy as np

def submatrix_with_particular_sum(matrix, target_sum=416):
    rows, cols = matrix.shape
    submatrices_list = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == target_sum:
                        submatrices_list.append(submatrix)
    return submatrices_list