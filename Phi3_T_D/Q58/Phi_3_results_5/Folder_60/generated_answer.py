import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if (k - i + 1) * (l - j + 1) == 88:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        count += int(np.sum(submatrix.reshape(-1) == 88) == 88)
    return count