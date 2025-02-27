import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 106):
        for j in range(cols - 106):
            if np.count_nonzero(matrix[i:i + 107, j:j + 107]) == 107:
                count += 1
    return count