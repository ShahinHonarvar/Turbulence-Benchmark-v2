import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    total_elements = rows * cols
    for size in range(1, total_elements + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == -97:
                    result.append(matrix[i:i + size, j:j + size].tolist())
    return result