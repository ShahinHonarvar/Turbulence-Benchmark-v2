import numpy as np

def submatrix_with_particular_sum(matrix):

    def _is_valid_submatrix(submatrix, target_sum=93):
        return np.array(submatrix).sum() == target_sum

    def _get_all_submatrices(matrix):
        rows, cols = matrix.shape
        for row_sz in range(1, rows + 1):
            for col_sz in range(1, cols + 1):
                for row_start in range(rows - row_sz + 1):
                    for col_start in range(cols - col_sz + 1):
                        yield matrix[row_start:row_start + row_sz, col_start:col_start + col_sz]
    result = []
    for submatrix in _get_all_submatrices(matrix):
        if _is_valid_submatrix(submatrix):
            result.append(submatrix)
    return result