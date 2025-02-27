import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 104):
        for j in range(cols - 104):
            if np.sum(matrix[i:i + 115, j:j + 115]) == 115:
                count += 1
    return count