import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 75):
        for j in range(num_cols - 75):
            submatrix = matrix[i:i + 76, j:j + 76]
            if submatrix.size == 76:
                count += 1
    return count