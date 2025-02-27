import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 84
    count = 0
    for i in range(rows):
        for j in range(cols):
            for width in range(1, cols - j + 1):
                height = target_size // width
                if target_size % width == 0 and i + height <= rows:
                    if np.prod(matrix[i:i + height, j:j + width].shape) == target_size:
                        count += 1
    return count