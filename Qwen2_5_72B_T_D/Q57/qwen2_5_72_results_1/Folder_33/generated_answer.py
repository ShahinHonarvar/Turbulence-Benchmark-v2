import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, target_sum):
        for top in range(row + 1):
            for left in range(col + 1):
                for bottom in range(top, row + 1):
                    for right in range(left, col + 1):
                        submatrix = matrix[top:bottom + 1, left:right + 1]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix.tolist())
    result = []
    num_rows, num_cols = matrix.shape
    find_submatrices(num_rows, num_cols, -811)
    return result