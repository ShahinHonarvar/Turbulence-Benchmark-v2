import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submats = []
        for i in range(rows):
            for j in range(cols):
                for row_end in range(i + 1, rows + 1):
                    for col_end in range(j + 1, cols + 1):
                        sub = matrix[i:row_end, j:col_end]
                        submats.append(sub)
        return submats
    submats = submatrices(matrix, matrix.shape[0], matrix.shape[1])
    result = [sub for sub in submats if np.sum(sub) == 432]
    return result