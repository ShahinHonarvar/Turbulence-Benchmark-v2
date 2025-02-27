import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i, matrix.shape[0]):
                for n in range(j, matrix.shape[1]):
                    sub_matrix = matrix[i:m + 1, j:n + 1]
                    if np.sum(sub_matrix) == -44:
                        result.append(sub_matrix)
    return result