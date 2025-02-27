import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(submatrix, target, start, end, result):
        for i in range(start, end + 1):
            for j in range(i + 1, end + 2):
                if np.sum(submatrix[i:j, :]) == target:
                    result.append(submatrix[i:j, :])
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    find_submatrices_with_sum(matrix, -97, i, k - 1, result)
    return result