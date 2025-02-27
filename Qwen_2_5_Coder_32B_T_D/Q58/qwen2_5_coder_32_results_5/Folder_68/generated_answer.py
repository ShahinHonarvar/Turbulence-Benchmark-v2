import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 8 < rows and j + 8 < cols:
                submatrix = matrix[i:i + 9, j:j + 9]
                if np.count_nonzero(submatrix == 74) == 74:
                    count += 1
    return count