import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 144:
                for k in range(i, rows):
                    if (k + 1 - i) * (cols - j + 1) == 144:
                        submatrix = matrix[i:k + 1, j:cols]
                        if np.prod(submatrix) == 144 ** 144:
                            count += 1
    return count