import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 129):
        for j in range(cols - 129):
            if matrix[i:i + 130, j:j + 130].size == 130:
                count += 1
    return count