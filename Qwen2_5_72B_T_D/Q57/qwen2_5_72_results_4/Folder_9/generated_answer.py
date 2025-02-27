import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submatrices.append(matrix[i:k, j:l])
        return submatrices
    target_sum = -86
    submatrices = get_submatrices(matrix)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == target_sum]
    return result