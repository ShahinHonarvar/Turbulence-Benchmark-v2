import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 22):
        for j in range(cols - 22):
            if np.sum(matrix[i:i + 23, j:j + 23] == 23) == 529:
                count += 1
    return count