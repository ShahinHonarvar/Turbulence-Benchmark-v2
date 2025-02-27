import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i + 1, min(i + 4, rows + 1)):
                for n in range(j + 1, min(j + 4, cols + 1)):
                    if np.sum(matrix[i:m, j:n]) == 27:
                        results.append(matrix[i:m, j:n])
    return results