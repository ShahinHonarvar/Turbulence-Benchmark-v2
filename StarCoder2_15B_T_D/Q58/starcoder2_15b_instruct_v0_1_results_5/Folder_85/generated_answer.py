import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_numbers = 13
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == num_numbers:
                count += 1
    return count