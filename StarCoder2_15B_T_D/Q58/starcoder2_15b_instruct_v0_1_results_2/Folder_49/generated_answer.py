import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.shape[0] < 9 or matrix.shape[1] < 9:
        return 0
    count = 0
    for i in range(matrix.shape[0] - 8):
        for j in range(matrix.shape[1] - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if submatrix.size == 72:
                count += 1
    return count