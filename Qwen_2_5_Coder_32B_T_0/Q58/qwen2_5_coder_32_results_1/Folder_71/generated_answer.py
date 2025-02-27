import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 77):
        for j in range(cols - 77):
            if np.sum(matrix[i:i + 78, j:j + 78]) == 78:
                count += 1
    return count