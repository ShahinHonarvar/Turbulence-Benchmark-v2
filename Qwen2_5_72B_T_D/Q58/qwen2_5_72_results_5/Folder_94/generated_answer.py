import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    target_elements = 93
    rows, cols = matrix.shape
    for i in range(rows - 9):
        for j in range(cols - 10):
            if np.sum((matrix[i:i + 10, j:j + 10] == target_elements).astype(int)) == target_elements:
                submatrix_count += 1
    return submatrix_count