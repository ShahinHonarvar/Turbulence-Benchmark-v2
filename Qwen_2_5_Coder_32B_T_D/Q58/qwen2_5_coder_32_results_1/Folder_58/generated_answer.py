import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 184):
        for j in range(cols - 184):
            if np.size(matrix[i:i + 185, j:j + 185]) == 185:
                count += 1
    return count