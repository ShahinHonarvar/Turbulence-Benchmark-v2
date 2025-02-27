import numpy as np

def submatrix_with_particular_sum(matrix):

    def gen_submatrices(matrix):
        rows, cols = matrix.shape
        return [matrix[top:bottom + 1, left:right + 1] for top in range(rows) for left in range(cols) for bottom in range(top, rows) for right in range(left, cols)]
    submatrices = gen_submatrices(matrix)
    return [np.array(subm) for subm in submatrices if subm.sum() == 752]