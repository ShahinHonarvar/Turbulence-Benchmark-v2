import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top + 1, rows + 1):
                    for right in range(left + 1, cols + 1):
                        submatrices.append(mat[top:bottom, left:right])
        return submatrices
    submatrices = get_all_submatrices(matrix)
    result = [submat.tolist() for submat in submatrices if submat.sum() == 19]
    return result