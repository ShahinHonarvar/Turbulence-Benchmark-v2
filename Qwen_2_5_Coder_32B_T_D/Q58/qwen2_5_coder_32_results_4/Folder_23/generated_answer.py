import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_sum = 69
    for i in range(rows):
        for j in range(cols):
            for sub_row in range(i + 1, rows + 1):
                for sub_col in range(j + 1, cols + 1):
                    if np.sum(matrix[i:sub_row, j:sub_col]) == target_sum:
                        count += 1
    return count