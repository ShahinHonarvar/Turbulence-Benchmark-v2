import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 47
    target_size = 2
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - target_size + 1):
        for j in range(cols - target_size + 1):
            submatrix = matrix[i:i + target_size, j:j + target_size]
            if np.count_nonzero(submatrix == target_count) == target_count:
                count += 1
    return count