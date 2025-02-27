import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 56):
        for j in range(cols - 56):
            if np.sum(matrix[i:i + 8, j:j + 8] == 57) == 64:
                count += 1
    return count