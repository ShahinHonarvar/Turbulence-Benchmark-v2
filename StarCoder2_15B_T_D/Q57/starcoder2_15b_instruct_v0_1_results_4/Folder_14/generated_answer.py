import numpy as np

def submatrix_with_particular_sum(matrix):
    """Finds all submatrices in the given matrix such that the sum of all integers in each submatrix equals -93.

    Args:
        matrix (np.ndarray): A two-dimensional numpy matrix of integers.

    Returns:
        list: A list of all submatrices that satisfy the condition.
    """

    def helper(matrix, target, row_start, row_end, col_start, col_end, result):
        if row_start == row_end or col_start == col_end:
            return
        for row in range(row_start, row_end):
            for col in range(col_start, col_end):
                sub_matrix = matrix[row:row_end, col:col_end]
                if sub_matrix.sum() == target:
                    result.append(sub_matrix)
        helper(matrix, target, row_start + 1, row_end, col_start + 1, col_end, result)
        helper(matrix, target, row_start, row_end - 1, col_start, col_end - 1, result)
        helper(matrix, target, row_start + 1, row_end - 1, col_start + 1, col_end - 1, result)
    result = []
    helper(matrix, -93, 0, matrix.shape[0], 0, matrix.shape[1], result)
    return result