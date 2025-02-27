import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    target_size = 51
    count = 0
    for i in range(m - int(np.sqrt(target_size)) + 1):
        for j in range(n - int(np.sqrt(target_size)) + 1):
            if np.prod(matrix[i:i + int(np.sqrt(target_size)), j:j + int(np.sqrt(target_size))].shape) == target_size:
                count += 1
    return count