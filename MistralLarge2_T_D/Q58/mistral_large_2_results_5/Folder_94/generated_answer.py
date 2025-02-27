import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def is_valid_submatrix(submatrix):
        return np.size(submatrix) == 93
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if is_valid_submatrix(submatrix):
                        count += 1
    return count