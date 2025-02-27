import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 3):
        for j in range(cols - 4):
            if np.size(matrix[i:i + 4, j:j + 5]) == 15:
                count += 1
    return count