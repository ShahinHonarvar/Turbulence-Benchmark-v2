import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            for x in range(i, nrows):
                for y in range(j, ncols):
                    submatrix = matrix[i:x + 1, j:y + 1].tolist()
                    if sum(map(sum, submatrix)) == 17:
                        result.append(submatrix)
    return result