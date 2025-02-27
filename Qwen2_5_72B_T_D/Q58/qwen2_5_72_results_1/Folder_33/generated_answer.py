import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 118
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    if np.count_nonzero(matrix[i:x, j:y]) == target_count:
                        count += 1
    return count