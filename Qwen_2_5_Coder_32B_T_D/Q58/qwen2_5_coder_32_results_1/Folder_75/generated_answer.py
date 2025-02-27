import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 79):
        for j in range(cols - 79):
            if np.size(matrix[i:i + 80, j:j + 80]) == 80:
                count += 1
    return count