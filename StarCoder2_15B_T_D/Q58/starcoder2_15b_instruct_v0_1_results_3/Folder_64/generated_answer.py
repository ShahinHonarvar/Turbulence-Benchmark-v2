import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    n = 7
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            num_integers = np.count_nonzero(submatrix)
            if num_integers == n:
                num_submatrices += 1
    return num_submatrices