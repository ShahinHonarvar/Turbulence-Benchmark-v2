import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m - 2):
        for j in range(n - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if sub_matrix.sum() == 66:
                result.append(sub_matrix)
    return result