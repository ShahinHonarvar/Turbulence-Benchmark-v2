import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 73
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for r in range(1, rows - i + 1):
                for c in range(1, cols - j + 1):
                    current_matrix = matrix[i:i + r, j:j + c]
                    if np.count_nonzero(current_matrix == 73) == target_count:
                        count += 1
    return count