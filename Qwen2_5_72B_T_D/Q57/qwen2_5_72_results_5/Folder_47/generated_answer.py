import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start, target_sum):
        rows, cols = matrix.shape
        result = []
        for row_end in range(start[0] + 1, rows + 1):
            for col_end in range(start[1] + 1, cols + 1):
                submatrix = matrix[start[0]:row_end, start[1]:col_end]
                if np.sum(submatrix) == target_sum:
                    result.append(submatrix)
        return result
    rows, cols = matrix.shape
    all_submatrices = []
    for i in range(rows):
        for j in range(cols):
            all_submatrices.extend(find_submatrices((i, j), 27))
    return all_submatrices