import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 98):
        for j in range(cols - 98):
            submatrix = matrix[i:i + 99, j:j + 99]
            if np.all(submatrix == 99):
                count += 1
    return count