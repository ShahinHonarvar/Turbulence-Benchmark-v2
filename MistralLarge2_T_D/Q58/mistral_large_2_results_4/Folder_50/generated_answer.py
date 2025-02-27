import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    if (k - i + 1) * (l - j + 1) == 40:
                        count += 1
    return count