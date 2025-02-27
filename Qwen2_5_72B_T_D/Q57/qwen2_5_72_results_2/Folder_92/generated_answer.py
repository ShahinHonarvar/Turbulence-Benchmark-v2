import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submatrices_list = []
        for i in range(rows):
            for j in range(cols):
                for width in range(1, cols - j + 1):
                    for height in range(1, rows - i + 1):
                        submatrices_list.append(matrix[i:i + height, j:j + width])
        return submatrices_list
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == -3]
    return result