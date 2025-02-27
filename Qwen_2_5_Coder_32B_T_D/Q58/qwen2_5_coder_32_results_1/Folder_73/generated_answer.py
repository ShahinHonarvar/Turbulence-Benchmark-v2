import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 41
    rows, cols = matrix.shape
    submatrix_size = int(np.sqrt(n))
    if submatrix_size ** 2 != n:
        return 0
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            if np.sum(matrix[i:i + submatrix_size, j:j + submatrix_size]) == n:
                count += 1
    return count