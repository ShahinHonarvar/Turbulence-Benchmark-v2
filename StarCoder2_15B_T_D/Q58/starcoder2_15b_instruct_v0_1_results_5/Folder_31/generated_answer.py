import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, column_count = matrix.shape
    submatrix_count = 0
    for i in range(row_count - 2):
        for j in range(column_count - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 45:
                submatrix_count += 1
    return submatrix_count