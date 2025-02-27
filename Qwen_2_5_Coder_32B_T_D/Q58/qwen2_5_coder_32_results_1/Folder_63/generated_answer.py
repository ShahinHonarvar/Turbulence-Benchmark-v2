import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 56):
        for j in range(cols - 56):
            if np.all(matrix[i:i + 57, j:j + 57] == 57):
                count += 1
    return count