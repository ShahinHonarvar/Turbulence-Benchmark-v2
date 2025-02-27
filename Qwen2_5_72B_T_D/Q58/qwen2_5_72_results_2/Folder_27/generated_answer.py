import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 77
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for row_end in range(i + 1, rows + 1):
                for col_end in range(j + 1, cols + 1):
                    if np.sum(matrix[i:row_end, j:col_end] == target_count) == target_count:
                        count += 1
    return count