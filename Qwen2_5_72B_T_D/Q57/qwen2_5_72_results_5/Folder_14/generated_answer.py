import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix):
        submatrices = []
        rows, cols = matrix.shape
        for top_row in range(rows):
            for bottom_row in range(top_row, rows):
                for left_col in range(cols):
                    for right_col in range(left_col, cols):
                        sub = matrix[top_row:bottom_row + 1, left_col:right_col + 1]
                        submatrices.append(sub)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [sub.tolist() for sub in submatrices if np.sum(sub) == -93]
    return result