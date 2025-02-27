import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 58):
        for j in range(cols - 58):
            submatrix = matrix[i:i + 59, j:j + 59]
            if submatrix.size == 59 ** 2:
                count += 1
    return count