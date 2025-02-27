import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 146
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for sub_row in range(i, rows):
                for sub_col in range(j, cols):
                    if (sub_row - i + 1) * (sub_col - j + 1) == target:
                        count += 1
    return count