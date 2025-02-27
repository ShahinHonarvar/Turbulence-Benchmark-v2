import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 19):
        for j in range(cols - 19):
            if np.size(matrix[i:i + 20, j:j + 20]) == 400:
                count += 1
    return count