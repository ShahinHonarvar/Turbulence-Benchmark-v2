import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 91
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 9 + 1):
        for j in range(cols - 9 + 1):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.size(submatrix) == target_size:
                count += 1
    return count