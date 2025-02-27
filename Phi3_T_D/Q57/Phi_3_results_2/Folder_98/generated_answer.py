import numpy as np

def submatrix_with_particular_sum(matrix):
    results = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = np.subtract(matrix[i:k + 1, j:l + 1], matrix[:k - i + 1, :l - j + 1]).sum(axis=(1, 2))
                    if np.all(submatrix == 0):
                        results.append(matrix[i:k + 1, j:l + 1])
    return results