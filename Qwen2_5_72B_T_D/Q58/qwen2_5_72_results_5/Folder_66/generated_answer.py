import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 42
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target:
                for r in range(i, rows):
                    for c in range(j, cols):
                        if np.sum(matrix[i:r + 1, j:c + 1] == target) == target:
                            count += 1
    return count