import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 77
    return_list = []
    m, n = matrix.shape
    for x in range(m):
        for y in range(n):
            for dx in range(x, m):
                for dy in range(y, n):
                    submatrix = matrix[x:dx + 1, y:dy + 1]
                    if np.sum(submatrix) == target_sum:
                        return_list.append(submatrix)
    return return_list