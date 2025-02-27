import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        sub_matrices = []
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        sub_matrices.append(matrix[i:k, j:l])
        return sub_matrices
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == 84]
    return result