import numpy as np

def submatrix_with_n_numbers(matrix):
    count, rows, cols = (0, matrix.shape[0], matrix.shape[1])
    for i in range(rows - 2):
        for j in range(cols - 2):
            if np.size(matrix[i:i + 3, j:j + 3]) == 13:
                count += 1
    return count