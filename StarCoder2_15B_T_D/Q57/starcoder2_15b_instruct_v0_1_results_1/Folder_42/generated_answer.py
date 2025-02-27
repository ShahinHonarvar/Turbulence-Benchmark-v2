import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            sub_matrix = np.array([[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]])
            if np.sum(sub_matrix) == 862:
                result.append(sub_matrix)
    return result