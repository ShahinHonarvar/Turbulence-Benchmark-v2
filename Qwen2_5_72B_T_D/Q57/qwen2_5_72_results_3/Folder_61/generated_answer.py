import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(mat, r, c):
        for size in range(1, min(r, c) + 1):
            for i in range(r - size + 1):
                for j in range(c - size + 1):
                    yield mat[i:i + size, j:j + size]
    result = []
    mat = np.array(matrix)
    rows, cols = mat.shape
    for sub in submatrices(mat, rows, cols):
        if np.sum(sub) == 8:
            result.append(sub.tolist())
    return result