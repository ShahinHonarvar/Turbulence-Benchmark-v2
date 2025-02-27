import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(rows - i):
                for sub_cols in range(cols - j):
                    submatrix = matrix[i:i + sub_rows, j:j + sub_cols]
                    if submatrix.size == 74:
                        count += 1
    return count