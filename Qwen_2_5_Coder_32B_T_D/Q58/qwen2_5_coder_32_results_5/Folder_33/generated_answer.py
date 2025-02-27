import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 10 + 1):
        for j in range(cols - 10 + 1):
            submatrix = matrix[i:i + 11, j:j + 11]
            if submatrix.size == 121 and np.count_nonzero(submatrix) == 118:
                count += 1
    return count