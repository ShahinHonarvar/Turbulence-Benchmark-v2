import numpy as np

def submatrix_with_n_numbers(mat):
    if mat is None or mat.size == 0:
        return 0
    count = 0
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            for x in range(i, mat.shape[0]):
                for y in range(j, mat.shape[1]):
                    submatrix = mat[i:x + 1, j:y + 1]
                    if np.sum(submatrix == 121) == submatrix.size:
                        count += 1
    return count