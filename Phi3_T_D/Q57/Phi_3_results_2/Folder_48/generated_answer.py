import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size_row in range(i + 1, rows + 1):
                for size_col in range(j + 1, cols + 1):
                    submatrix = matrix[i:size_row, j:size_col]
                    if submatrix.sum() == -261:
                        submatrices.append(submatrix)
    return submatrices