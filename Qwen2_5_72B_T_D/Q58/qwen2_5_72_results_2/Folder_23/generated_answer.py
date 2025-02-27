import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 69
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(1, rows - i + 1):
                for c in range(1, cols - j + 1):
                    if np.sum(matrix[i:i + r, j:j + c] == target) == 69:
                        count += 1
    return count