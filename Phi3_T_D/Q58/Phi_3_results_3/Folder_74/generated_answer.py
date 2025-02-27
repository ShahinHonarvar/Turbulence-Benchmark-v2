import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for width in range(cols - j + 1):
                for height in range(rows - i + 1):
                    if width * height == 48:
                        count += 1
    return count