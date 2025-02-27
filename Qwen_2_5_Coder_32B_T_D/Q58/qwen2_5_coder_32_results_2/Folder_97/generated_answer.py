import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 120
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            if np.prod(matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))].shape) == n:
                count += 1
    return count