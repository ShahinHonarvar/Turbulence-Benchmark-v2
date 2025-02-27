import numpy as np

def submatrix_with_n_numbers(matrix):
    if not matrix.size % 72 == 0:
        return 0
    total_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 72 <= rows and j + 72 <= cols:
                submatrix = matrix[i:i + 72, j:j + 72]
                if np.all(submatrix):
                    total_count += 1
    return total_count