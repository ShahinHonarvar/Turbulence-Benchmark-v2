import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 4):
        for j in range(cols - 4):
            if np.sum(matrix[i:i + 5, j:j + 5]) == 53:
                count += 1
    return count