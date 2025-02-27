import numpy as np

def submatrix_with_n_numbers(matrix):
    target_number = 179
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - target_number + 1):
        for j in range(cols - target_number + 1):
            if np.sum(matrix[i:i + target_number, j:j + target_number]) == target_number:
                count += 1
    return count