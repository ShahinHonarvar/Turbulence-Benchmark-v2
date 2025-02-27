import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 76):
        for j in range(cols - 76):
            if np.sum(matrix[i:i + 77, j:j + 77] == 77) == 77 * 77:
                count += 1
    return count