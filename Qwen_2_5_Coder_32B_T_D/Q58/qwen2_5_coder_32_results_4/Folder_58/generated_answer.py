import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 17 + 1):
        for j in range(cols - 17 + 1):
            if np.sum(matrix[i:i + 18, j:j + 18]) == 185:
                count += 1
    return count