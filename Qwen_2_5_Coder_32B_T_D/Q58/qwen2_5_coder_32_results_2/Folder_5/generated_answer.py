import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 7 + 1):
        for j in range(cols - 7 + 1):
            if np.array_equal(matrix[i:i + 7, j:j + 7], 63):
                count += 1
    return count