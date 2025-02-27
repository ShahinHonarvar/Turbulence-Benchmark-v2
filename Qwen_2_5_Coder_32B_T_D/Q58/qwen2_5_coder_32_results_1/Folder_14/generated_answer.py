import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows < 84 or cols < 84:
        return 0
    for i in range(rows - 83):
        for j in range(cols - 83):
            if np.sum(matrix[i:i + 84, j:j + 84]) == 84:
                count += 1
    return count