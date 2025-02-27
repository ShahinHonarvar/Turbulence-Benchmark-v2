import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    result = []
    for i in range(rows):
        for j in range(columns):
            for x in range(i, rows):
                for y in range(j, columns):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if np.sum(submatrix) == 40:
                        result.append(submatrix.tolist())
    return result