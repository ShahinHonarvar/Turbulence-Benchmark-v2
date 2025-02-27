import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows < 4 or cols < 4:
        return count
    for i in range(rows - 3):
        for j in range(cols - 3):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 180:
                count += 1
    return count