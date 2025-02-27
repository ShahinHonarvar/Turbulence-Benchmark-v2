import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, start_i, start_j, end_i, end_j):
        submatrices_list = []
        for i in range(start_i, end_i + 1):
            for j in range(start_j, end_j + 1):
                submatrix = matrix[i:end_i, j:end_j]
                if np.sum(submatrix) == -9:
                    submatrices_list.append(submatrix)
        return submatrices_list
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i + 1, rows + 1):
                for y in range(j + 1, cols + 1):
                    result.extend(submatrices(matrix, i, j, x, y))
    return result