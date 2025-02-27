import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                sub = np.sum(matrix[i:i + size, j:j + size])
                if sub == 27:
                    results.append(matrix[i:i + size, j:j + size])
    return results