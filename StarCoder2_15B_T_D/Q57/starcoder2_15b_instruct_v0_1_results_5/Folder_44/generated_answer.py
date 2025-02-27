import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, columns = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for column_start in range(columns):
                for column_end in range(column_start + 1, columns + 1):
                    submatrix = matrix[row_start:row_end, column_start:column_end]
                    if submatrix.sum() == 830:
                        result.append(submatrix)
    return result