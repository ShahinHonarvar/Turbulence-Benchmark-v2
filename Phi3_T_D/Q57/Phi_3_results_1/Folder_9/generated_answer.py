import numpy as np

def submatrix_with_particular_sum(matrix):
    size_x, size_y = matrix.shape
    result = []
    for i in range(size_x):
        for j in range(size_y):
            for k in range(i, size_x):
                for l in range(j, size_y):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == -86:
                        result.append(submatrix)
    return result