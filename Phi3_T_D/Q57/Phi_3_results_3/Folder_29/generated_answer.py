import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = [matrix[i:i + j, k:k + l] for i in range(matrix.shape[0]) for j in range(i, matrix.shape[0]) for k in range(matrix.shape[1]) for l in range(k, matrix.shape[1])]
    selected_submatrices = [mat for mat in submatrices if np.sum(mat) == 84]
    return selected_submatrices