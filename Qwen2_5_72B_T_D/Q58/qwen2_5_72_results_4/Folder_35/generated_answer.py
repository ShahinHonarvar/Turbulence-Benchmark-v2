import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 111
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_size:
                submat_size = 1
                while i + submat_size <= rows and j + submat_size <= cols:
                    if np.sum(matrix[i:i + submat_size, j:j + submat_size] == target_size) == submat_size ** 2:
                        count += 1
                    submat_size += 1
    return count