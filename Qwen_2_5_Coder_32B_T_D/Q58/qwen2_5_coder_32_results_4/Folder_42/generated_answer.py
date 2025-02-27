import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 182):
        for j in range(cols - 182):
            if np.sum(matrix[i:i + 193, j:j + 193]) == 193:
                count += 1
    return count