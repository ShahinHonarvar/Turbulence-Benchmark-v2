import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 72):
        for j in range(cols - 72):
            if np.sum(matrix[i:i + 9, j:j + 9] == 73) == 81:
                count += 1
    return count