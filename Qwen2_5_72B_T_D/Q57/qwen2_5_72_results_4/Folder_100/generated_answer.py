import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(submat, target_sum):
        submatrices = []
        rows, cols = submat.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        if np.sum(submat[i:k, j:l]) == target_sum:
                            submatrices.append(submat[i:k, j:l].tolist())
        return submatrices
    return submatrix_sum(matrix, 28)