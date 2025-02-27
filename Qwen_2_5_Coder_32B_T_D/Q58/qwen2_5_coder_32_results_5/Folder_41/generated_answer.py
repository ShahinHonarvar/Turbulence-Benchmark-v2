import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows * cols < 73:
        return 0
    for i in range(rows - 73 + 1):
        for j in range(cols - 73 + 1):
            if np.size(matrix[i:i + 73, j:j + 73]) == 73:
                count += 1
    return count