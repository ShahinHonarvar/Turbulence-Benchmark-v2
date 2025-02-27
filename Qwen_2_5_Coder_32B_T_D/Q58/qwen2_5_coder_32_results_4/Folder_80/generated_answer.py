import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    submatrix_size = 180
    count = 0
    if submatrix_size > rows * cols:
        return 0
    for i in range(rows - int(np.sqrt(submatrix_size)) + 1):
        for j in range(cols - int(np.sqrt(submatrix_size)) + 1):
            if np.sum(matrix[i:i + int(np.sqrt(submatrix_size)), j:j + int(np.sqrt(submatrix_size))]) == submatrix_size:
                count += 1
    return count