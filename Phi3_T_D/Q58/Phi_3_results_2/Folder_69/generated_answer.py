import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if j + 11 < cols and i + 11 < rows:
                submatrix = matrix[i:i + 12, j:j + 12]
                if np.all(submatrix == 126):
                    count += 1
    return count