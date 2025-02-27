import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 185):
        for j in range(cols - 185):
            if np.sum(matrix[i:i + 186, j:j + 186]) == 186:
                count += 1
    return count