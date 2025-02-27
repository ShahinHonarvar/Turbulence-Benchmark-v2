import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    submatrix_size = 96 ** 0.5
    if not submatrix_size.is_integer():
        return 0
    submatrix_size = int(submatrix_size)
    for i in range(rows - submatrix_size + 1):
        for j in range(cols - submatrix_size + 1):
            if np.sum(matrix[i:i + submatrix_size, j:j + submatrix_size] == 96) == 96:
                count += 1
    return count