import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 92
    rows, cols = matrix.shape
    if rows * cols < target_count:
        return 0
    count = 0
    for i in range(rows - 9 + 1):
        for j in range(cols - 10 + 1):
            if np.sum((matrix[i:i + 9, j:j + 10] == target_count).flatten()) == target_count:
                count += 1
    return count