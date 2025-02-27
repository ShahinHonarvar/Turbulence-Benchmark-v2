import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum_zero(mat):
        row, col = (len(mat), len(mat[0]))
        result = []
        for start_row in range(row):
            for end_row in range(start_row, row):
                sum_matrix = np.zeros((1, col))
                for r in range(start_row, end_row + 1):
                    sum_matrix += mat[r, :]
                for start_col in range(col):
                    current_sum = 0
                    sum_dict = {0: -1}
                    for end_col in range(start_col, col):
                        current_sum += sum_matrix[0, end_col]
                        if current_sum in sum_dict:
                            result.append(mat[start_row:end_row + 1, start_col:end_col + 1])
                        sum_dict[current_sum] = end_col
        return result
    return find_submatrices_with_sum_zero(matrix)