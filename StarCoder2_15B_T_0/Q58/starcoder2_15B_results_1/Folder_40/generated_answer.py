import numpy as np

def submatrix_with_n_numbers(matrix, n=1):
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.count_nonzero(submatrix) == n:
                        count += 1
    return count