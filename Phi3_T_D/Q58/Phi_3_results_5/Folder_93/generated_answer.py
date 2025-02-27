import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    rows, cols = (matrix.shape[0], matrix.shape[1])
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix == 53) == submatrix.size:
                        total_count += 1
    return total_count