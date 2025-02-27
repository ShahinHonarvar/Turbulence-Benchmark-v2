import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 72
    count = 0
    for i in range(rows - 8 + 1):
        for j in range(cols - 9 + 1):
            if (rows - i) * (cols - j) >= target_size:
                if np.sum(matrix[i:i + 8, j:j + 9].flatten() == matrix[i:i + 8, j:j + 9]) == target_size:
                    count += 1
    return count