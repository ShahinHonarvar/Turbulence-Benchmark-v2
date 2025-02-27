import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 8):
        for j in range(cols - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.size(submatrix) == 81 and np.all(submatrix == 91):
                count += 1
    return count