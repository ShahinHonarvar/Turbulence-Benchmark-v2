import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        submat = mat[i:p, j:q]
                        if np.sum(submat) == target_sum:
                            result.append(submat)
        return result
    return find_submatrices_with_sum(matrix, -811)