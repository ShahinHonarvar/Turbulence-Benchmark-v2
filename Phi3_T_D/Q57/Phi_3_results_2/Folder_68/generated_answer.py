import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def includes_sum(r, c, size):
        return np.sum(matrix[r:r + size, c:c + size]) == 3
    for i in range(rows):
        for j in range(cols):
            for size in range(1, rows - i + 1):
                if i + size <= rows and j + size <= cols and includes_sum(i, j, size):
                    result.append(matrix[i:i + size, j:j + size].tolist())
    return result