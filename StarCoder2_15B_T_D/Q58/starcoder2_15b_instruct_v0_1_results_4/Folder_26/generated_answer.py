import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 114):
        for j in range(num_cols - 114):
            submatrix = matrix[i:i + 115, j:j + 115]
            if submatrix.size == 115:
                count += 1
    return count