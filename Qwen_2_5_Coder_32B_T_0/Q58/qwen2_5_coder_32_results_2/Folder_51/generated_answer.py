import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 94):
        for j in range(cols - 94):
            if np.sum(matrix[i:i + 95, j:j + 95] == 95) == 95:
                count += 1
    return count