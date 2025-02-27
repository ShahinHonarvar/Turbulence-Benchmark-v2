import numpy as np

def submatrix_with_n_numbers(matrix, n=48):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size_row in range(i, rows):
                for size_col in range(j, cols):
                    submatrix = matrix[i:size_row + 1, j:size_col + 1]
                    if submatrix.size == n:
                        count += 1
    return count