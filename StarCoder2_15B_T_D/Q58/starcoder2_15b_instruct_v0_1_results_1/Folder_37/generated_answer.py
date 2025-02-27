import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 7):
        for j in range(num_cols - 7):
            submatrix = matrix[i:i + 8, j:j + 8]
            if submatrix.size == 64:
                count += 1
    return count