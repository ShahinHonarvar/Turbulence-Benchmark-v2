import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 40
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) >= target_size:
                for size_x in range(1, rows - i + 1):
                    for size_y in range(1, cols - j + 1):
                        if size_x * size_y == target_size:
                            count += 1
    return count