import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 42):
        for j in range(cols - 42):
            if np.all(matrix[i:i + 43, j:j + 43] == 43):
                count += 1
    return count