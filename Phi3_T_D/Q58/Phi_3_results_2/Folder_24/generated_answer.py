import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = (matrix.shape[0], matrix.shape[1])
    count = 0
    for size in range(1, min(height, width) + 1):
        for h_start in range(height - size + 1):
            for w_start in range(width - size + 1):
                if np.all(matrix[h_start:h_start + size, w_start:w_start + size]):
                    count += 1
    return count