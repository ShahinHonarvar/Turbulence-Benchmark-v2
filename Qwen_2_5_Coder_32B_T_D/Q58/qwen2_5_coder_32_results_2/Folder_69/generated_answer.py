import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 126
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - int(np.sqrt(target_size)) + 1):
        for j in range(cols - int(np.sqrt(target_size)) + 1):
            if np.prod(matrix[i:i + int(np.sqrt(target_size)), j:j + int(np.sqrt(target_size))].shape) == target_size:
                count += 1
    return count