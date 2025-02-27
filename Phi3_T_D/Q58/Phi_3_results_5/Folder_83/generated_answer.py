import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 47
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                end_i = min(k, rows)
                for l in range(j + 1, cols + 1):
                    end_j = min(l, cols)
                    submatrix = matrix[i:end_i, j:end_j]
                    if np.sum(submatrix == n) == np.size(submatrix):
                        count += 1
    return count