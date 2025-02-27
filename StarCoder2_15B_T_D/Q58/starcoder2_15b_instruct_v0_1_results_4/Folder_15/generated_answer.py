import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if np.count_nonzero(submatrix) == 2:
                num_submatrices += 1
    return num_submatrices