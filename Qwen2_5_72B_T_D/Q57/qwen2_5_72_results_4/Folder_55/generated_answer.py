import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(mat, target_sum):
        rows, cols = mat.shape
        result = []
        for r in range(rows):
            for c in range(cols):
                for r_step in range(1, rows - r + 1):
                    for c_step in range(1, cols - c + 1):
                        submat = mat[r:r + r_step, c:c + c_step]
                        if np.sum(submat) == target_sum:
                            result.append(submat)
        return result
    return find_submatrices(matrix, 1)