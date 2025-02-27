import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    row_count, column_count = matrix.shape
    for row_start in range(row_count):
        for row_end in range(row_start + 1, row_count + 1):
            for column_start in range(column_count):
                for column_end in range(column_start + 1, column_count + 1):
                    submatrix = matrix[row_start:row_end, column_start:column_end]
                    if submatrix.sum() == -87:
                        submatrices.append(submatrix)
    return submatrices