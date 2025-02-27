import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 93
    count = 0

    def count_submatrices_with_target(row, col):
        nonlocal count
        current_sum = 0
        for i in range(row, rows):
            current_sum += sum(matrix[i, col:cols])
            if current_sum == target_count:
                count += 1
    for start_row in range(rows):
        for start_col in range(cols):
            count_submatrices_with_target(start_row, start_col)
    return count