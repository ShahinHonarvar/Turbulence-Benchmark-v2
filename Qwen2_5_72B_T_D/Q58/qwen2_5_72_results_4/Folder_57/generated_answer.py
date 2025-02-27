import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 92
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_count:
                submatrix_count += 1
                for k in range(i, rows):
                    for l in range(j, cols):
                        if matrix[k, l] == target_count:
                            submatrix_count += 1
    for size in range(2, max(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.sum(matrix[i:i + size, j:j + size] == target_count) == 92:
                    submatrix_count += 1
    return submatrix_count if submatrix_count > 0 else 0