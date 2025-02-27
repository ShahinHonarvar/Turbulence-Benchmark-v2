import numpy as np

def submatrix_with_n_numbers(matrix):
    nrows, ncols = matrix.shape
    count = 0
    for size in range(1, min(nrows, ncols) + 1):
        for i in range(nrows - size + 1):
            for j in range(ncols - size + 1):
                if np.all(matrix[i:i + size, j:j + size] == size ** 2):
                    count += 1
    return count