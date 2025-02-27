import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(matrix, rows, cols):
        submatrices = []
        for i in range(rows):
            for j in range(cols):
                for p in range(i + 1, rows + 1):
                    for q in range(j + 1, cols + 1):
                        submatrices.append(matrix[i:p, j:q])
        return submatrices
    rows, cols = matrix.shape
    submatrices = generate_submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == 16]
    return result