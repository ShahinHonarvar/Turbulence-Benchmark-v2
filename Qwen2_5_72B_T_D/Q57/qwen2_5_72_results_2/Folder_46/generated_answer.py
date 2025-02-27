import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for r in range(rows):
            for c in range(cols):
                for i in range(r + 1, rows + 1):
                    for j in range(c + 1, cols + 1):
                        submatrices.append(mat[r:i, c:j])
        return submatrices
    target_sum = 416
    result = []
    submatrices = get_submatrices(matrix)
    for sub in submatrices:
        if np.sum(sub) == target_sum:
            result.append(sub)
    return result