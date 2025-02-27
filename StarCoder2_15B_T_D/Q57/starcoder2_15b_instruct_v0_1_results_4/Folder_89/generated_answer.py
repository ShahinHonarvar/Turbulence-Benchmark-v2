import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m - 1):
        for j in range(n - 1):
            sub_matrix = matrix[i:i + 2, j:j + 2]
            if sub_matrix.sum() == 80:
                result.append(sub_matrix)
    return result