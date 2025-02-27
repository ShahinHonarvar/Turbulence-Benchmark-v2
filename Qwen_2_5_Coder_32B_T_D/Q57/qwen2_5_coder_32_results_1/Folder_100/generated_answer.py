import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for row_end in range(i, m):
                for col_end in range(j, n):
                    submatrix = matrix[i:row_end + 1, j:col_end + 1]
                    if submatrix.sum() == 28:
                        result.append(submatrix)
    return result