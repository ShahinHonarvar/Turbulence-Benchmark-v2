import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 5, -1, -1):
        for j in range(cols - 7, -1, -1):
            if np.size(matrix[i:i + 6, j:j + 7]) == 40:
                count += 1
    return count