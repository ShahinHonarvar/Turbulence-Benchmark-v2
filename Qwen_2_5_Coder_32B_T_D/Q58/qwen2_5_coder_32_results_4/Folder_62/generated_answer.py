import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    if rows * cols < 186:
        return 0
    for i in range(rows - 186 // cols + 1):
        for j in range(cols - 186 % cols + 1):
            submatrix = matrix[i:i + 186 // cols, j:j + 186 % cols]
            if submatrix.size == 186 and np.prod(submatrix.shape) == 186:
                count += 1
    return count