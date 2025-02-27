import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for x_len in range(1, cols - c + 1):
                for y_len in range(1, rows - r + 1):
                    if x_len * y_len == 53:
                        submatrix = matrix[r:r + y_len, c:c + x_len]
                        if np.prod(submatrix.shape) == 53:
                            count += 1
    return count