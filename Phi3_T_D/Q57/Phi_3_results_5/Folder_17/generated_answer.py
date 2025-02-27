import numpy as np

def submatrix_with_particular_sum(matrix):

    def helper(r1, c1, r2, c2):
        submatrix_sum = np.sum(matrix[r1:r2, c1:c2])
        return submatrix_sum == 398

    def search_submatrices(starting_row, starting_col):
        submatrices = []
        for sub_rows in range(starting_row, len(matrix)):
            for sub_cols in range(starting_col, len(matrix[0])):
                if helper(starting_row, starting_col, sub_rows + 1, sub_cols + 1):
                    submatrices.append(matrix[starting_row:sub_rows + 1, starting_col:sub_cols + 1])
        return submatrices
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result.extend(search_submatrices(i, j))
    return result