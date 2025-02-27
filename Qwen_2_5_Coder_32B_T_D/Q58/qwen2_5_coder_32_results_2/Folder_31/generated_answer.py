import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 6):
        for j in range(cols - 6):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.sum(submatrix == 45) == 45:
                count += 1
    return count