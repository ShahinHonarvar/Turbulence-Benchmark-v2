import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum):

        def check_submatrix_sum(submatrix, target_sum):
            return np.sum(submatrix) == target_sum
        rows, cols = mat.shape
        result = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrix = mat[start_row:end_row, start_col:end_col]
                        if check_submatrix_sum(submatrix, target_sum):
                            result.append(submatrix)
        return result
    return find_submatrices_with_sum(matrix, -157)