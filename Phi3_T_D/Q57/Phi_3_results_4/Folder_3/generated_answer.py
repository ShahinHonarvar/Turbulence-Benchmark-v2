import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_cumulative_sum(matrix):
        cum_sum = np.zeros((matrix.shape[0] + 1, matrix.shape[1] + 1))
        cum_sum[1:, 1:] = np.cumsum(np.cumsum(matrix, axis=0), axis=1)
        return cum_sum

    def find_submatrices(cum_sum, target_sum, rows, cols):
        submatrices = []
        for top in range(rows):
            for left in range(cols):
                for bottom in range(top, rows):
                    for right in range(left, cols):
                        current_sum = cum_sum[bottom + 1, right + 1] - cum_sum[bottom + 1, left] - cum_sum[top, right + 1] + cum_sum[top, left]
                        if current_sum == target_sum:
                            submatrices.append(matrix[top:bottom + 1, left:right + 1])
        return submatrices
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2 or (not matrix.dtype.kind in 'ui'):
        return []
    cum_sum = get_cumulative_sum(matrix)
    return find_submatrices(cum_sum, 54, *matrix.shape)