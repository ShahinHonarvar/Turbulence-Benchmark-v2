import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix):
        rows, cols = matrix.shape
        submats = []
        for i in range(rows):
            for j in range(cols):
                for row_end in range(i, rows):
                    for col_end in range(j, cols):
                        submat = matrix[i:row_end + 1, j:col_end + 1]
                        submats.append(submat)
        return submats
    result = [submat for submat in submatrices(matrix) if np.sum(submat) == -308]
    return result