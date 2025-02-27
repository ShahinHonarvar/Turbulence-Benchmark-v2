import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    if matrix.size == 0:
        return 0
    rows, cols = matrix.shape
    target_size = 54
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    if height * width == target_size:
                        submatrix = matrix[i:i + height, j:j + width]
                        count += 1
    return count