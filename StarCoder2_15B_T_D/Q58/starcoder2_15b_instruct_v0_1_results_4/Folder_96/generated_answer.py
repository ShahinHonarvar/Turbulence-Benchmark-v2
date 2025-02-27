import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 19):
        for j in range(num_cols - 19):
            submatrix = matrix[i:i + 20, j:j + 20]
            if submatrix.size == 20:
                count += 1
    return count