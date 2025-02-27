import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows):
                for l in range(j + 1, cols):
                    if k - i == 3 and l - j == 3:
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if np.prod(submatrix) == 8 or np.sum(submatrix) == 8:
                            count += 1
    return count