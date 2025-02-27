import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submats = []
        for i in range(rows):
            for j in range(cols):
                for width in range(1, cols - j + 1):
                    for height in range(1, rows - i + 1):
                        submats.append(matrix[i:i + height, j:j + width])
        return submats
    rows, cols = matrix.shape
    submats = submatrices(matrix, rows, cols)
    filtered_submats = [submat for submat in submats if np.sum(submat) == -87]
    return filtered_submats