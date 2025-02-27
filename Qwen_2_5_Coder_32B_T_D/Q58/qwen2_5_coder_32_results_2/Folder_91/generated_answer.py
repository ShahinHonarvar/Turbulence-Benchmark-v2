import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if np.size(matrix[i:i + 2, j:j + 2]) == 4:
                count += 1
    for i in range(rows - 2):
        for j in range(cols - 2):
            if np.size(matrix[i:i + 3, j:j + 3]) == 9:
                count += 4
            if np.size(matrix[i:i + 3, j:j + 2]) == 6:
                count += 2
            if np.size(matrix[i:i + 2, j:j + 3]) == 6:
                count += 2
    return count if count > 0 else 0