import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 94):
        for j in range(cols - 94):
            if np.count_nonzero(matrix[i:i + 10, j:j + 10]) == 95:
                count += 1
    return count