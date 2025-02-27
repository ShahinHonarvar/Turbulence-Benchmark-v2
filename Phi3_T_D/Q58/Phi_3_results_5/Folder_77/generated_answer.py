import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for n_rows in range(1, rows + 1):
        for n_cols in range(1, cols + 1):
            for i in range(rows - n_rows + 1):
                for j in range(cols - n_cols + 1):
                    submatrix = matrix[i:i + n_rows, j:j + n_cols]
                    if np.sum(submatrix == 179) == int(np.prod(submatrix.shape)):
                        count += 1
    return count