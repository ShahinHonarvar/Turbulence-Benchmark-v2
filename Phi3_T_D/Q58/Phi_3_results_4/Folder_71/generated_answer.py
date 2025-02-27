import numpy as np

def submatrix_with_n_numbers(matrix):
    sub_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if np.all(matrix[i:k + 1, j:l + 1].flatten() == 78):
                        sub_count += 1
    return sub_count