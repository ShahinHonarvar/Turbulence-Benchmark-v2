import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submatrices_list = []
        for top in range(rows):
            for bottom in range(top, rows):
                for left in range(cols):
                    for right in range(left, cols):
                        submatrices_list.append(matrix[top:bottom + 1, left:right + 1])
        return submatrices_list
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == 41]
    return result