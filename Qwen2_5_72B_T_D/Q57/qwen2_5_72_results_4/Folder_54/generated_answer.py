import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submats = []
        for i in range(rows):
            for j in range(cols):
                for row_size in range(1, rows - i + 1):
                    for col_size in range(1, cols - j + 1):
                        submats.append(matrix[i:i + row_size, j:j + col_size])
        return submats
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    target_sum = -59
    result = [submat for submat in all_submatrices if np.sum(submat) == target_sum]
    return result