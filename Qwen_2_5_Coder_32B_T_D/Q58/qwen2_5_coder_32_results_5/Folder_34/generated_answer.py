import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 82):
        for j in range(cols - 82):
            if np.sum(matrix[i:i + 9, j:j + 9] == 83) == 81:
                count += 1
    return count