import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 46):
        for j in range(cols - 46):
            if np.all(matrix[i:i + 7, j:j + 7] == 47):
                count += 1
    return count