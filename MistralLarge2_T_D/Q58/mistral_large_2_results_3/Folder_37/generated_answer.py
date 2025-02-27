import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 64
    submatrix_size = int(np.sqrt(target_size))
    count = 0
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            if np.count_nonzero(matrix[i:i + submatrix_size, j:j + submatrix_size]) == target_size:
                count += 1
    return count