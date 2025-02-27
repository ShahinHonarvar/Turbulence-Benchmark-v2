import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submat = mat[i:k, j:l]
                        if np.sum(submat) == target_sum:
                            result.append(submat)
        return result
    return find_submatrices_with_sum(matrix, 80)