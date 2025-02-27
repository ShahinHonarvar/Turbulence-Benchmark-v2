import numpy as np

def submatrix_with_particular_sum(input_matrix):
    submatrices = []
    for i in range(input_matrix.shape[0]):
        for j in range(input_matrix.shape[1]):
            for k in range(i, input_matrix.shape[0]):
                for l in range(j, input_matrix.shape[1]):
                    submatrix = input_matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -15:
                        submatrices.append(submatrix)
    return submatrices