import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 40
    if n > rows * cols:
        return 0
    for i in range(rows - int(np.sqrt(n)) + 1):
        for j in range(cols - int(np.sqrt(n)) + 1):
            if np.sum(matrix[i:i + int(np.sqrt(n)), j:j + int(np.sqrt(n))]) == n:
                count += 1
    return count