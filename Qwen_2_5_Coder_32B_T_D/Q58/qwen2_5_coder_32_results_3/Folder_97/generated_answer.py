import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 11):
        for j in range(cols - 11):
            if np.size(matrix[i:i + 11, j:j + 11]) == 120:
                count += 1
    return count