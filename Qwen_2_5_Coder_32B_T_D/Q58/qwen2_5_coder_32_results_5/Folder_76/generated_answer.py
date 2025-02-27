import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_size = 159
    if target_size > rows * cols:
        return 0
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    if height * width == target_size:
                        if np.sum(matrix[i:i + height, j:j + width]) == target_size:
                            count += 1
    return count