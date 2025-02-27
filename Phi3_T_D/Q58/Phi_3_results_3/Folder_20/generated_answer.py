import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 49
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if j + n <= cols:
                sub_matrix = matrix[i:i + 1, j:j + n]
                count += np.all(sub_matrix == matrix[i, j])
    return count