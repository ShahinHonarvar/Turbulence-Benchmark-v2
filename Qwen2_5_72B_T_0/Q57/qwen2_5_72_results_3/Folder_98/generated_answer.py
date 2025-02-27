import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum_zero(mat):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                sum_matrix = np.zeros((1, col), dtype=int)
                for r in range(start_row, end_row + 1):
                    sum_matrix[0] += mat[r]
                    if np.sum(sum_matrix) == 0:
                        result.append(sum_matrix)
        return result
    return find_submatrices_with_sum_zero(matrix)