import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x_size in range(1, rows - i + 1):
                for y_size in range(1, cols - j + 1):
                    submatrix = matrix[i:i + x_size, j:j + y_size]
                    if submatrix.size == 107:
                        count += 1
    return count