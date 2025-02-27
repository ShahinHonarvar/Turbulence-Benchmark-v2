import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 9 + 1):
        for j in range(cols - 9 + 1):
            if np.sum(matrix[i:i + 9, j:j + 9]) == 96:
                count += 1
    return count