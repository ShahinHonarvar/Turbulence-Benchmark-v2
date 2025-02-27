import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 88
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target:
                for r in range(i + 1, rows + 1):
                    for c in range(j + 1, cols + 1):
                        if np.sum(matrix[i:r, j:c] == target) == 88:
                            count += 1
    return count