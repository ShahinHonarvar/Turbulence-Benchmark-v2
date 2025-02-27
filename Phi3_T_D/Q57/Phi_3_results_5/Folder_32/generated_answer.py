import numpy as np

def submatrix_with_particular_sum(matrix):

    def wrapper(matrix):
        m, n = matrix.shape
        result = []
        for i in range(m):
            for j in range(n):
                for k in range(i, m):
                    for l in range(j, n):
                        submatrix = matrix[i:k + 1, j:l + 1]
                        if submatrix.sum() == 901:
                            result.append(submatrix.tolist())
        return result
    return wrapper(matrix)