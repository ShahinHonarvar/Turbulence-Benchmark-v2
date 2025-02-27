import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_count, col_count = matrix.shape
    for i in range(row_count - 3):
        for j in range(col_count - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 193:
                count += 1
    return count