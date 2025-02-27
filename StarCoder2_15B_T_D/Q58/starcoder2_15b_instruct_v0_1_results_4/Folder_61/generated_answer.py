import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 4
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            num_integers = np.count_nonzero(~np.isnan(submatrix))
            if num_integers == n:
                count += 1
    return count