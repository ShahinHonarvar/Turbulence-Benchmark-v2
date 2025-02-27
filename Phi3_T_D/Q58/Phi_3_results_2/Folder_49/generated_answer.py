import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 72
    height, width = matrix.shape
    count = 0
    for i in range(height):
        for j in range(width):
            for size_height in range(1, height - i + 1):
                if size_height * width < n:
                    continue
                for size_width in range(1, width - j + 1):
                    if size_height * size_width < n:
                        continue
                    if size_height * size_width == n:
                        count += 1
    return count