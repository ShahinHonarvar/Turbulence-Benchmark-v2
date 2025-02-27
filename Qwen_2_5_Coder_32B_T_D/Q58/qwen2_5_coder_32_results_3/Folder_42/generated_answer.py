import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    if matrix.size < 193:
        return count
    rows, cols = matrix.shape
    for i in range(rows - 12):
        for j in range(cols - 16):
            if matrix[i:i + 13, j:j + 17].size == 193:
                count += 1
    return count