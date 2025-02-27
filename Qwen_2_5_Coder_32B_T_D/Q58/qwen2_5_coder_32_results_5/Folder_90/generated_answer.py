import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    if matrix.size < 176:
        return count
    rows, cols = matrix.shape
    for row in range(rows - 11):
        for col in range(cols - 16):
            if np.size(matrix[row:row + 12, col:col + 16]) == 176:
                count += 1
    return count