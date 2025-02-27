import numpy as np

def submatrix_with_particular_sum(matrix):

    def is_valid_submatrix_sum(submatrix):
        return np.sum(submatrix) == 0

    def get_submatrices(row, col, rows, cols, mat):
        submatrices = []
        for i in range(row + 1):
            for j in range(col + 1):
                sub = mat[i:row + 1, j:col + 1]
                if is_valid_submatrix_sum(sub):
                    submatrices.append(sub)
        return submatrices
    mat = np.array(matrix)
    rows, cols = mat.shape
    result = []
    for row in range(rows):
        for col in range(cols):
            result.extend(get_submatrices(row, col, rows, cols, mat))
    return result