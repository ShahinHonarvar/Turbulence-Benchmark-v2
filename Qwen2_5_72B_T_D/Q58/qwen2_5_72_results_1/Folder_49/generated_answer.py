import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 72
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 8 + 1):
        for j in range(cols - 9 + 1):
            if (rows - i) * (cols - j) >= target_size:
                if np.size(matrix[i:i + 9, j:j + 8]) == target_size:
                    count += 1
    return count