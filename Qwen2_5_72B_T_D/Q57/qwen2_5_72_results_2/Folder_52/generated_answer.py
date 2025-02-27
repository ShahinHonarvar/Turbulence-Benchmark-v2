import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, result):
        rows, cols = mat.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        submat = mat[start_row:end_row, start_col:end_col]
                        if np.sum(submat) == target_sum:
                            result.append(submat.tolist())
        return result
    return find_submatrices_with_sum(np.array(matrix), 100, [])